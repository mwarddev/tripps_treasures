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

// Handle card validation errors
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

    var saveInfo = Boolean($('#save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': client_secret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(client_secret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.phone.value),
                    address: {
                        line1: $.trim(form.address_line1.value),
                        line2: $.trim(form.address_line2.value),
                        city: $.trim(form.city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.shp_full_name.value),
                // phone: $.trim(form.phone.value),
                address: {
                    line1: $.trim(form.shp_address_line1.value),
                    line2: $.trim(form.shp_address_line2.value),
                    city: $.trim(form.shp_city.value),
                    state: $.trim(form.shp_county.value),
                    postal_code: $.trim(form.shp_postcode.value),
                    country: $.trim(form.shp_country.value),
                }
            }
            // shipping: {
            //     name: $.trim(form.full_name.value),
            //     phone: $.trim(form.phone.value),
            //     address: {
            //         line1: $.trim(form.shp_address_line1.value),
            //         line2: $.trim(form.shp_address_line2.value),
            //         city: $.trim(form.shp_city.value),
            //         state: $.trim(form.shp_county.value),
            //         postal_code: $.trim(form.shp_postcode.value),
            //         country: $.trim(form.shp_country.value),
            //     }
            // }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fa-solid fa-circle-exclamation"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({ 'disabled': false});
                $('#submit-purchase').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    })
});
