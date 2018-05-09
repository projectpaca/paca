$(function () {

  // funktionen startar

    $('#calendar').fullCalendar({
        //visuell formatering av kalendern
        header: {
            left: 'month,agendaWeek,agendaDay',
            center: 'title',
            right: 'prev, next'
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
        
        eventRender: function (event, element) {
            var start = moment(event.start).fromNow();
            element.attr('title', start);
        },
        
        //funktionalitet i kalendern
        weekends: true,
        editable: true,
        eventDurationEditable: true,
        eventStartEditable: true,
        selectable: true,
        selectHelper: true,

        select: function (start, end, jsEvent, view) {
            endtime = $.fullCalendar.formatDate(end, 'h:mm tt');
            starttime = $.fullCalendar.formatDate(start, 'ddd, MMM d, h:mm tt')
            var duration = (starttime - endtime);
            if (duration === 30) {
                end = start.add(30, 'mins');
            return $('#calendar').fullCalendar('select', start, end);
            }
            
            var title = prompt('Skriv in titel på passet:', "Nytt pass");

            if (title != null) {
                var event = {
                    title: title,
                    start: start,
                    end: end
                };
            $("#calendar").fullCalendar('renderEvent', event, true,
    ['stick']);
            };
                
               /* && title.trim()) {
                var eventData = {
                    title: title,
                    start: start,
                    end: end
                }; */
                console.log(title, start, end);        
    
            // Add event
        $.ajax({
            url: "new",
            type: "POST",
            data: {
                title: title,
                start: start,
                end: end,
            },
            dataType: "JSON"
        }).done(function (data) {
            $("#calendar").fullCalendar("renderEvent", data);
        });
        
    }, //select 
    });// function fullcalendar
});//function
        

$('#calendar').fullCalendar('next');

$('#calendar').fullCalendar({
    eventSources: [
        {
            url: 'events'
        }
    ],

    DayClick: function (date, jsEvent) {
        console.log('day', date.format()); // date is a moment
        console.log('coords', jsEvent.pageX, jsEvent.pageY);
    } // länkar siffran (dagens datum) i kalendern till specifika sidan för den dagen

});

/*
$("#calendar").fullCalendar('renderEvent', {
                            start: start,
                            end: end,
                            title: title
                            }
 },
    ['stick'],
                        true);
*/
