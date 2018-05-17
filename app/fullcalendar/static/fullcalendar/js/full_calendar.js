/*global $, jQuery*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';'),
            i = 0;
        for (i; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(function () {

  // funktionen startar

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
        handleWindowResize: true,
        slotEventOverlap: true,
        eventLimit: true,
        
        //översätter default namn till svenska
        allDayText: "Heldag",
        noEventsMessage: "Inga händelser att visa",
        buttonText: {
            today: 'idag',
            month: 'månad',
            week: 'vecka',
            day: 'dag'
        },
        // översätter namnen på månaderna till svenska
        monthNames: [
            'Januari', 'Februari', 'Mars',
            'April', 'Maj', 'Juni', 'Juli',
            'Augusti', 'September', 'Oktober',
            'November', 'December'
        ],
        // översätter namnen på dagarna till svenska
        dayNamesShort: [
            'Mån', 'Tis', 'Ons', 'Tors',
            'Fre', 'Lör', 'Sön'
        ],
        
        //tid och tidsformatering
        timeFormat: 'H:mm',
        displayEventTime: true,
        defaultTimedEventDuration: '02:00:00',
        
        
        //funktionalitet i kalendern
        weekends: true,
        //editable: true,
        eventDurationEditable: true,
        eventStartEditable: true,
        eventSources: [{
            url: 'events'
        }],
        eventMouseover: function (data, event, view) {

            tooltip = '<div class="tooltiptopicevent" style="width:auto;height:auto;background:#FFE4B5;position:absolute;z-index:10001;padding:10px 10px 10px 10px ;  line-height: 200%;">' + 'Titel: ' + data.title + '</br>' + 'Börjar: ' + data.start.format('YYYY-MM-DD hh:mm') + '</br>' + 'Slutar: ' + data.end.format('YYYY-MM-DD hh:mm') + '</div>';


            $("body").append(tooltip);
            $(this).mouseover(function (e) {
                $(this).css('z-index', 10000);
                $('.tooltiptopicevent').fadeIn('500');
                $('.tooltiptopicevent').fadeTo('10', 1.9);
            }).mousemove(function (e) {
                $('.tooltiptopicevent').css('top', e.pageY + 10);
                $('.tooltiptopicevent').css('left', e.pageX + 20);
            });


        },
        eventMouseout: function (data, event, view) {
            $(this).css('z-index', 8);

            $('.tooltiptopicevent').remove();

        },
            
        eventRender: function (event, element, view) {
            
            if (event.title === 'Kassa') {
                element.css('eventBackgroundColor', '#B2FF66');
                
            } else if (event.title === 'Lager') {
                element.css('eventBackgroundColor', '#FF3333');
            
            } else if (event.title === 'Chark') {
                element.css('eventBackgroundColor', '#66B2FF'); 
            }

        },
        eventColor: '#FFCCCC'  
    });
});

$('#calendar').fullCalendar('next');


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