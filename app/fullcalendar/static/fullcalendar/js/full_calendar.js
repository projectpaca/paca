$(function () {

  // funktionen startar

    $('#calendar').fullCalendar({
        //visuell formatering av kalendern
        header: {
            left: 'prev, next',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        weekNumbers: true,
        weekNumberTitle: 'Vecka',
        defaultView: 'agendaWeek',
        titleFormat: 'MMMM YYYY',
        handleWindowResize: true,
        
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
        timeZone: 'local',
        timeFormat: 'H:mm',
        displayEventTime: true,
        
        //funktionalitet i kalendern
        weekends: true,
        editable: true,
        eventDurationEditable: true,
        eventStartEditable: true,
        selectable: true,
        selectHelper: true,

        select: function (startDate, endDate, allDay, jsEvent, view) {
            var duration = (end - start);
            if (duration === 30) {
                end = start.add(30, 'mins');
                return $('#calendar').fullCalendar('select', start, end);

            }
            
            var title = prompt('Skriv in titel på passet:');
            var eventData;
            if (title && title.trim()) {
                eventData = {
                    title: title,
                    start: start,
                    end: end
                };
                console.log(title, start, end);

                eventSources[
                    {
                        url: 'events'
                    }
                ];
                
                $('#calendar').fullCalendar('dayClick', function (date, jsEvent) {
                    var chosenDate = date.format();
                    $("#start").val(chosenDate);
                    $("#end").val(chosenDate);
                    $("#exampleModal").modal("show");
                });
            };
    
            // Add event
            $("#save-event").on("click", function () {
                var title = $("#title").val();
                var start = $("#start").val();
                var end = $("#end").val();
       
                $.ajax({
                    url: "/save-event",
                    type: "POST",
                    data: {
                        start: start,
                        end: end,
                        title: title
                    },
                    dataType: "JSON"
                }).done(function (data) {
                    $("#calendar").fullCalendar("renderEvent", data);
                    $("#exampleModal").modal("hide");
                });
        
        
            });
        }
    });
});
        

$('#calendar').fullCalendar('next');