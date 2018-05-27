/* global $, jQuery */

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';'),
            i = 0;
        for (i; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    // Creates cookie
}

$(function () {
    $('#calendar').fullCalendar({
        // Customization of PACA calendar
        // Mainly translation to Swedish
        header: {
            left: '',
            center: 'prev, title, next',
            right: 'month,agendaWeek,agendaDay'
        },
        weekNumbers: true,
        firstDay: 1,
        weekNumberTitle: 'Vecka',
        defaultView: 'agendaWeek',
        titleFormat: 'MMMM YYYY',
        views: {
            month: {
                columnHeaderFormat: 'ddd'
            },
            week: {
                columnHeaderFormat: 'ddd D/M'
            },
            day: {
                columnHeaderFormat: 'dddd'
            }
        },
        handleWindowResize: true,
        slotEventOverlap: true,
        eventLimit: true,
        weekends: true,
        allDayText: "Heldag",
        noEventsMessage: "Inga händelser att visa",
        buttonText: {
            today: 'idag',
            month: 'månad',
            week: 'vecka',
            day: 'dag'
        },
        monthNames: [
            'Januari', 'Februari', 'Mars',
            'April', 'Maj', 'Juni', 'Juli',
            'Augusti', 'September', 'Oktober',
            'November', 'December'
        ],
        dayNamesShort: [
            'Sön', 'Mån', 'Tis', 'Ons', 'Tors',
            'Fre', 'Lör'
        ],
        dayNames: [
            'Söndag', 'Måndag', 'Tisdag', 'Onsdag',
            'Torsdag', 'Fredag', 'Lördag'
        ],

        timeFormat: 'H:mm',
        slotLabelFormat: 'HH:mm',
        minTime: '05:00:00',
        maxTime: '22:00:00',
        displayEventTime: true,

        eventSources: [{
            url: 'events'
        }],
        lazyFetching: true,

        // Mouseover modal with information about a single shift
        eventMouseover: function (data, event, view) {
            tooltip = '<div class="tooltiptopicevent" style="width:auto;height:auto;background:#FFE4B5;position:absolute;z-index:10001;padding:10px 10px 10px 10px ;  line-height: 200%;">' + 'Pass:  ' + data.title_id + '</br> Börjar: ' + data.start.format('YYYY-MM-DD hh:mm') + '</br> Slutar: ' + data.end.format('YYYY-MM-DD hh:mm') + '</div>';
            $("body").append(tooltip);
            $(this).mouseover(function (e) {
                $(this).css('z-index', 10000);
                $('.tooltiptopicevent').fadeIn('500');
                $('.tooltiptopicevent').fadeTo('10', 1.9);
            }).mousemove(function (e) {
                $('.tooltiptopicevent').css('top', e.pageY + 10);
                $('.tooltiptopicevent').css('left', e.pageX + 20);
            }); // Displays title/department, start, and end time at mouseover
        },

        eventMouseout: function (data, event, view) {
            $(this).css('z-index', 8);
            $('.tooltiptopicevent').remove();
        },

        eventRender: function (event, element, view) {
            var skift = event.title_id;
            if (skift === 'Kassa') {
                element.css('background-color', '#7CB1BB');
                // Hardcoding department "Kassa" to be turqoise 
            } else if (skift === 'Lager') {
                element.css('background-color', '#D63B3E');
                // Hardcoding department "Lager" to be red 
            } else if (skift === 'Chark') {
                element.css('background-color', '#EAA241');
                // Hardcoding department "Chark" to be orange 
            } else {
                element.css('background-color', '#E99481');
                // Hardcoding all other departments to be pink 
            }
            
        },

        eventClick: function (event, jsEvent, view) {
            if (confirm("Bekräfta bokning av pass" + '\n Pass:  ' + event.title_id + ' \n Börjar: ' + event.start.format('YYYY-MM-DD hh:mm') + '\n Slutar: ' + event.end.format('YYYY-MM-DD hh:mm'))) {
                console.log("boka mig på detta pass:");
                console.log(event);
                console.log(event.id);

                var csrftoken = getCookie('csrftoken'),
                    pk = {
                        "event_id": event.id
                    };
                console.log("TOKEN:");
                console.log(csrftoken);

                console.log(pk);
                console.log("Ovan är pass PK");

                $.ajax({
                    type: "POST",
                    url: 'upd_event',
                    headers: {
                        'X-CSRFToken': csrftoken
                    },
                    data: pk,
                    dataType: "json",

                    success: function () {
                        $(".confirm-message").show();
                        $(".confirm-message").text("Passet är bokat!").fadeIn().delay(5000).fadeOut();

                    },
                    error: function () {
                        $(".error-message").show();
                        $(".error-message").text("Bokning gick inte, passet är upptaget.").fadeIn().delay(5000).fadeOut();

                    }

                }).done(function (data) {
                    $("#calendar").fullCalendar("renderEvent", data);
                });

            } else {
                console.log("Ej bokat");
            }
        }
    }); //fullcalendar functionen
}); // function

$('#calendar').fullCalendar('next');
