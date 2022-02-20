$(function () {
  $('a[href^="#"]').click(function () {
    let anchor = $(this).attr('href');
    $('html, body').animate({
      scrollTop: $(anchor).offset().top
    }, 600);
  });

  // var currentLocation = window.location;
  // if (currentLocation.hash !== "") {
  //   $('html, body').animate({
  //     scrollTop: $(currentLocation.hash).offset().top
  //   }, 600);
  // }

  //var dotaBoostPrices = JSON.parse('{{ dota_prices_json | safe }}');

  var dotaBoostPrices = JSON.parse('[{ "model": "services.dotapriceboost", "pk": 1, "fields": { "mmr": 1000, "price": 60 } }, { "model": "services.dotapriceboost", "pk": 2, "fields": { "mmr": 2000, "price": 60 } }, { "model": "services.dotapriceboost", "pk": 3, "fields": { "mmr": 3000, "price": 70 } }, { "model": "services.dotapriceboost", "pk": 4, "fields": { "mmr": 4000, "price": 80 } }, { "model": "services.dotapriceboost", "pk": 5, "fields": { "mmr": 5000, "price": 85 } }, { "model": "services.dotapriceboost", "pk": 6, "fields": { "mmr": 6000, "price": 95 } }]');

  function renderDotaBoostPrice() {
    var resultPrice = 0;
    var desiredMmr = parseInt($('#desired-mmr').val());
    var selfMmr = parseInt($('#self-mmr').val());

    for (let i = 0; i < 50; i++) {
      if (selfMmr % 50 === 0) {
        break;
      }
      else {
        selfMmr = selfMmr + 1
      }
    }


    if (selfMmr > desiredMmr) {
      resultPrice = 0;
    }

    var countNeedMmr = desiredMmr - selfMmr;
    // console.log({selfMmr, desiredMmr, countNeedMmr, });

    if (countNeedMmr > 50) {
      var actualPrices = dotaBoostPrices.filter(o => o.fields.mmr > selfMmr && o.fields.mmr < desiredMmr + 1000);

      // console.log(actualPrices);
      for (let i = 0; i < actualPrices.length; i++) {
        var item = actualPrices[i];

        if (actualPrices.length === 1) {
          resultPrice = (desiredMmr - selfMmr) / 50 * item.fields.price
          break;
        }
        else {
          if (i === 0) {
            resultPrice = resultPrice + ((item.fields.mmr - selfMmr) / 50 * item.fields.price)
          }
          else if (i === actualPrices.length - 1) {
            if (item.fields.mmr < desiredMmr) {
              resultPrice = resultPrice + ((desiredMmr - item.fields.mmr + 1000) / 50 * item.fields.price)

            } else if (item.fields.mmr === desiredMmr) {
              resultPrice = resultPrice + ((1000) / 50 * item.fields.price)
            } else {
              resultPrice = resultPrice + ((desiredMmr - item.fields.mmr + 1000) / 50 * item.fields.price)
              // console.log((desiredMmr - item.fields.mmr + 1000));
              // console.log(desiredMmr);
              // console.log(item.fields.mmr);
            }
          }
          else {
            resultPrice = resultPrice + ((1000) / 50 * item.fields.price)
          }
        }
      }
    }

    var additopnalSevicesPercents = 0;
    var additopnalSevicesPrice = 0;

    var additopnalSevices = $(".dota-checkbox");
    $.each(additopnalSevices, (index, value) => {
      if (value.checked) {
        if (value.dataset.serviceType === "percent") {
          additopnalSevicesPercents = additopnalSevicesPercents + parseInt(value.dataset.value);
        } else {
          additopnalSevicesPrice = additopnalSevicesPrice + parseInt(value.dataset.value);
        }
      }
    });
    console.log();
    var additopnalSevicesPercentsPrice = resultPrice / 100 * additopnalSevicesPercents;

    resultPrice = resultPrice + additopnalSevicesPercentsPrice + additopnalSevicesPrice;
    $("#dota-boost-price").html(resultPrice);
  }

  $('.dota-checkbox').change(function () {
    renderDotaBoostPrice();
  });

  function renderCsgoBoostPrice() {
    var resultPrice = 0;
    var desiredRank = $('#desired-rank').find(":selected");
    var selfRank = $('#self-rank').find(":selected");

    if (parseInt(selfRank[0].dataset.order) < parseInt(desiredRank[0].dataset.order)) {

      $.each($("#self-rank option"), (index, value) => {

        if ((parseInt(value.dataset.order) > selfRank[0].dataset.order) &&
          (parseInt(value.dataset.order) <= desiredRank[0].dataset.order)) {
          resultPrice = resultPrice + parseInt(value.value);
        }

      });
    }


    var additopnalSevicesPercents = 0;
    var additopnalSevicesPrice = 0;
    var additopnalSevices = $(".csgo-checkbox");
    $.each(additopnalSevices, (index, value) => {
      if (value.checked) {
        if (value.dataset.serviceType === "percent") {
          additopnalSevicesPercents = additopnalSevicesPercents + parseInt(value.dataset.value);
        } else {
          additopnalSevicesPrice = additopnalSevicesPrice + parseInt(value.dataset.value);
        }
      }
    });
    var additopnalSevicesPercentsPrice = resultPrice / 100 * additopnalSevicesPercents;
    resultPrice = resultPrice + additopnalSevicesPercentsPrice + additopnalSevicesPrice;
    $("#csgo-boost-price").html(resultPrice);
  }

  $('#self-rank').change(function () {
    renderCsgoBoostPrice();
  });
  $('#desired-rank').change(function () {
    renderCsgoBoostPrice();
  });

  $('.csgo-checkbox').change(function () {
    renderCsgoBoostPrice();
  });
  var $document = $(document);
  var selector = '[data-rangeslider]';
  var $element = $(selector);

  var textContent = ('textContent' in document) ? 'textContent' : 'innerText';

  function valueOutput(element) {
    var value = element.value;
    var output = element.parentNode.getElementsByTagName('output')[0] || element.parentNode.parentNode.getElementsByTagName('output')[0];
    output[textContent] = value;
  }

  $document.on('input', 'input[type="range"], ' + selector, function (e) {
    valueOutput(e.target);
  });

  $document.on('click', '#js-example-disabled button[data-behaviour="toggle"]', function (e) {
    var $inputRange = $(selector, e.target.parentNode);

    if ($inputRange[0].disabled) {
      $inputRange.prop("disabled", false);
    }
    else {
      $inputRange.prop("disabled", true);
    }
    $inputRange.rangeslider('update');
  });

  $document.on('click', '#js-example-change-value button', function (e) {
    var $inputRange = $(selector, e.target.parentNode);
    var value = $('input[type="number"]', e.target.parentNode)[0].value;

    $inputRange.val(value).change();
  });

  $document.on('click', '#js-example-change-attributes button', function (e) {
    var $inputRange = $(selector, e.target.parentNode);
    var attributes = {
      min: $('input[name="min"]', e.target.parentNode)[0].value,
      max: $('input[name="max"]', e.target.parentNode)[0].value,
      step: $('input[name="step"]', e.target.parentNode)[0].value
    };
    $inputRange.attr(attributes);
    $inputRange.rangeslider('update', true);
  });

  $document
    .on('click', '#js-example-destroy button[data-behaviour="destroy"]', function (e) {
      $(selector, e.target.parentNode).rangeslider('destroy');
    })
    .on('click', '#js-example-destroy button[data-behaviour="initialize"]', function (e) {
      $(selector, e.target.parentNode).rangeslider({ polyfill: false });
    });

  $document
    .on('click', '#js-example-hidden button[data-behaviour="toggle"]', function (e) {
      var $container = $(e.target.previousElementSibling);
      $container.toggle();
    });

  $element.rangeslider({

    polyfill: false,

    onInit: function () {
      valueOutput(this.$element[0]);
    },

    onSlide: function (position, value) {
      //console.log('onSlide');
      //console.log('position: ' + position, 'value: ' + value);
      renderDotaBoostPrice();
    },

    onSlideEnd: function (position, value) {
      //console.log('onSlideEnd');
      //console.log('position: ' + position, 'value: ' + value);

    }
  });

});
