/*global $, jQuery*/
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
        editable: true,
        droppable: true,
        eventDurationEditable: true,
        eventStartEditable: true,
        eventSources: [
            {
                url: 'events'
            }],
        selectable: true,
        selectHelper: true,

        select: function (start, end, jsEvent, view) {
            var duration = (end - start) / 1000,
                title = prompt('Skriv in titel på passet:', "Nytt pass"),
                event = {
                    title: title,
                    start: start,
                    end: end
                };
            /*
            if (duration === 1800) {
                end = start.add(30, 'mins');
                return $('#calendar').fullCalendar('select', start, end);
            } */

            if (title !== null) {
                $("#calendar").fullCalendar('renderEvent', event, 'stick', true);
                
                $('#calendar').fullCalendar('unselect');
            }
            console.log(title, start, end);
            
            // Add event
            $.ajax({
                url: "new",
                type: "POST",
                data: {
                    title: title,
                    start: start,
                    end: end
                },
                dataType: "json"
            }).done(function (data) {
                $("#calendar").fullCalendar("renderEvent", data);
            });
            
        
        }, //select 
        eventRender: function (event, element) {
            var start = moment(event.start).fromNow();
            element.attr('title', start);
        }
        
    });// function fullcalendar
});//function
        

$('#calendar').fullCalendar('next');

$('#calendar').fullCalendar({
    DayClick: function (date, jsEvent) {
        console.log('day', date.format()); // date is a moment
        console.log('coords', jsEvent.pageX, jsEvent.pageY);
    } // länkar siffran (dagens datum) i kalendern till specifika sidan för den dagen

});