$(document).ready(function () {

    $('.calendar').each(function () {
        var calendar = $(this);
        calendar.fullCalendar({
            header: {
                left: 'prev, next, today',
                center: 'title',
                right: 'month, agendaWeek'
            },
        // För att även se helger
            weekends: true,
            
        // Gör det möjligt att klicka och välja i kalendern
            selectable: true,
            
        /*
            select: function(start, end, jsEvent, view) {
                var title = prompt("Skriv in titel på detta pass",
                    if (title != null) {
                        var event = {
                            title: title.trim() != "" ? title: "Nytt event",
                            start: start,
                            end: end
                        };

                    $calendar.fullCalendar("renderEvent", Event, true)
                    };
                    $calendar.fullCalendar("unselect");

                }
            } 
            */ 
            
            // Eventen ska vara möjliga att redigera
            editable: true
        });
            
    },
                        
                        )});
        
