var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Roboto", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
            <i class="fa-solid fa-circle-exclamation"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('purchase-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-purchase').attr('disabled', true);
    $('#purchase-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#save-user-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
            } //remove this brace before uncommenting billing details
//                 billing_details: {
//                     name: $.trim(form.full_name.value),
//                     phone: $.trim(form.phone_number.value),
//                     email: $.trim(form.email.value),
//                     address:{
//                         line1: $.trim(form.street_address1.value),
//                         line2: $.trim(form.street_address2.value),
//                         city: $.trim(form.town_or_city.value),
//                         country: $.trim(form.country.value),
//                         state: $.trim(form.county.value),
//                     }
//                 }
//             },
//             shipping: {
//                 name: $.trim(form.full_name.value),
//                 phone: $.trim(form.phone_number.value),
//                 address: {
//                     line1: $.trim(form.street_address1.value),
//                     line2: $.trim(form.street_address2.value),
//                     city: $.trim(form.town_or_city.value),
//                     country: $.trim(form.country.value),
//                     postal_code: $.trim(form.postcode.value),
//                     state: $.trim(form.county.value),
//                 }
//             },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fa-solid fa-circle-exclamation"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#purchase-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-purchase').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});
