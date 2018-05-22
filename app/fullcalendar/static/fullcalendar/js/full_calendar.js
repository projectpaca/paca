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
    // skapar en cookie
}

$(function () {
    $('#calendar').fullCalendar({
        //visuell formatering av kalendern
        header: {
            left: '',
            center: 'prev, title, next',
            right: 'month,agendaWeek,agendaDay'
        },
        weekNumbers: true,
        firstDay: 0,
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
            'Mån', 'Tis', 'Ons', 'Tors',
            'Fre', 'Lör', 'Sön'
        ],
        dayNames: [
            'Måndag', 'Tisdag', 'Onsdag',
            'Torsdag', 'Fredag', 'Lördag', 'Söndag'
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

        // när en håller musen över(hover) på ett pass så visas information, titel, start- och sluttid, i en ljusgul ruta
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
            }); //presenterar titel/avdelning, starttid och sluttid vid hover över pass
        },

        eventMouseout: function (data, event, view) {
            $(this).css('z-index', 8);
            $('.tooltiptopicevent').remove();
        },

        eventRender: function (event, element, view) {
            var skift = event.title_id;
            if (skift === 'Kassa') {
                element.css('background-color', '#B2FF66');
                // Gör passet grönt om det är 'kassa'
            } else if (skift === 'Lager') {
                element.css('background-color', 'red');
                // Gör passet rött om det är 'lager'
            } else if (skift === 'Chark') {
                element.css('background-color', '#66B2FF');
                // Gör passet blått om det är 'chark'
            } else {
                element.css('background-color', '#FFCCCC');
                // Gör passet rosa om det inte stämmer med ovan IF-satser
            }// END IF SATS
            
        }, //eventRender ger färg efter avdelning

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

// NEDAN TAS BORT?

// funktionen ovan ('next') kan ej tas bort, gör det möjligt att byta till nästa vecka och månad.
// Nedanstående kod har ingen funktion längre, men ligger hårt jobb bakom så nostalgist / Hanna


       /* select: function (start, end, jsEvent, view) {
            var duration = (end - start) / 1000,
                title = prompt('Skriv in titel på passet:', "Nytt pass"),
                req_usr = "1",
                dept = 'kassa',
                event = {
                    title: title,
                    start: moment(start).format('YYYY-MM-DD hh:mm'), // få ett datumformat
                    end: moment(end).format('YYYY-MM-DD hh:mm'), // end/start är innan ett objekt med tid, vi behöver en sträng för att skicka med i ajax
                    req_usr: req_usr,
                    dept: dept
                };

            if (duration === 1800) {
                end = start.add(30, 'mins');
                return $('#calendar').fullCalendar('select', start, end);
            }

            if (title !== null) {
                $("#calendar").fullCalendar('renderEvent', event, 'stick', true);

                $('#calendar').fullCalendar('unselect');
            }
            console.log(event); // logga vårt nya event
            // var csrftoken = Cookies.get('csrftoken');
            var csrftoken = getCookie('csrftoken');
            console.log(csrftoken);

            $('#calendar').fullcalendar({
                eventClick: function (event, jsEvent, view) {
                    if (alert("Vill du ta bort detta pass?")) {
                        $('#calendar').fullCalendar('removeEvents', event);
                    } else {
                        pass;
                    }

                    $('#calendar').fullCalendar('updateEvent', event);

                },

            }); */


    /*        // Lägg till event
    $.ajax({
        type: "POST",
        url: 'new',
        headers: {
            'X-CSRFToken': csrftoken
        },
                //+ JSON.stringify(event),
        data: event, // (titel, start, end, req_usr, dept)
        dataType: "json",
        success: function () {
            alert("YEEEYYY!");
        },
        error: function () {
            alert("nix inte idag...");
        }

    }).done(function (data) {
        $("#calendar").fullCalendar("renderEvent", data);
        $("#myModal").modal("hide");

    });


}); //select

*/

//    });// function fullcalendar
// });//function

/*
$('#calendar').fullCalendar({
    DayClick: function (date, jsEvent, view) {
        console.log('day', date.format()); // date is a moment
        console.log('coords', jsEvent.pageX, jsEvent.pageY);
    } // länkar siffran (dagens datum) i kalendern till specifika sidan för den dagen

});*/
