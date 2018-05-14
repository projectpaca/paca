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
        //eventLimitClick: function ( cellInfo, jsEvent) {},
        
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
                    start: moment(start).format('YYYY-MM-DD hh:mm'), // datumformat 
                    end: moment(end).format('YYYY-MM-DD hh:mm') // start/end är innan ett objekt med tid, behöver en sträng för att skicka med i ajax
                };

            if (title !== null) {
                $("#calendar").fullCalendar('renderEvent', event, 'stick', true);
                
                $('#calendar').fullCalendar('unselect');
            }
            console.log(event); //logga vårt nya event
            
            // Add event
            $.ajax({
                url: "new",
                type: "POST",
                data: event, //(titel, start, end)
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