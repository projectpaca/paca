//JavaScript kod från ramverket FullCalendar
// För projektet PACA, skivet av Hanna 
$(function() {

  // funktionen startar

    $('#calendar').fullCalendar({
        timeZone: 'local',
        defaultView: 'agendaWeek',
        fixedWeekCount: false,
        firstDay: 0, 
        // sätter första dagen i månaden & veckan till måndag
        weekNumbers: true,
        weekNumberTitle: 'Vecka',
        // skapar en kolumn för vecka samt ändrar kolumnens namn till 'Vecka'

        lazyFetching: false,
        /* Varje gång anävndaren klickar på någonting i kalendern kommer infomrmation hämtas
        användbart ifall det är många användare samtidigt. Motsvarigheten 'true' gör istället
        att all information hämtas in i för varje månad & går därför snabbare */
        handleWindowResize: true,
        // anpassar kalendern till fönstret

        header: {
            left: 'title',
            center: 'prev, next',
            right: 'month, agendaWeek, agendaMonth'
        },
        // fixerar headern så månaden står till vänster, pilarna för nästa & föregående i mitten och månad/vecka till höger
        buttonText: {
            today: 'idag',
            month: 'månad',
            week: 'vecka',
            day: 'dag'
        },
        eventLimit: true,
        slotEventOverlap: true,
        minTime: '05:00:00',
        maxTime: '22:00:00',
        // gör det möjligt för event att lägga sig över varandra
        events: [
            {
                title: 'TEST',
                start: '2018-04-20',
                end: '2018-04-20',
            }
        ], //ett hårdkodat event för test **
        displayEventTime: true,
        // senare när eventen har inskrivna start- och sluttid så kommer dessa visas
        monthNames: [
            'Januari', 'Februari', 'Mars',
            'April', 'Maj', 'Juni', 'Juli',
            'Augusti', 'September', 'Oktober',
            'November', 'December'
        ],
        // översätter namnen på månaderna till svenska
        dayNamesShort: [
            'Mån', 'Tis', 'Ons', 'Tors',
            'Fre', 'Lör', 'Sön'
        ],
        // översätter namnen på dagarna till svenska

        titleFormat: 'MMMM YYYY',
        // för att visa hela namnet på månaden samt året till vänster uppe i header
        timeFormat: 'h(:mm)',
        // visar tiden på pass. Som hela timmar enligt 24h klockan och minuter, ex 06.30
        weekends: true,
        editable: true,
        droppable: true,
        selectable: true,
        selectHelper: true,
        
        select: function(start, end) {
            var duration = (end - start) / 1000;
            if (duration === 1800) {
            // sätter default varaktighet till en timme
                end = start.add(30, 'mins');
                return $('#calendar').fullCalendar('select', start, end);
            }
            var title = prompt('Event Title:');
            var eventData;
            if (title && title.trim()) {
                eventData = {
                    title: title,
                    start: start,
                    end: end
                };
                
                /*
                    Ska göra ett ajax-anrop till Django,
                    som ska spara händelsen i databasen.
                */
                $.ajax({
                    url: "/calendar/new",
                    data: {
                        title: "TEST"
                    }
                }).done(function (data) {
                    // Denna funktionen körs när man får ett svar på ajax-anropet
                    // Parametern "data" är den information som kommer från Django
                    
                    if (data === true) {
                        alert("Din bokning har sparats!")
                    } else if (data === false) {
                        alert("FEL! Din bokning sparades inte...")
                    } else {
                        pass
                    }
                });

                $('#calendar').fullCalendar('renderEvent', {
                    start: start,
                    end: end,
                    title: title
                },  'stick',
                    true);
            }
            $('#calendar').fullCalendar('unselect');
        },
        
        eventRender: function(event, element) {
            var start = moment(event.start).fromNow();
            element.attr('title', start);
        },
        loading: function() {
      
        }
        
        /* räknar ut hur länge ett event är från start- och sluttid. Kontrollerar att eventet är 
        tillräckligt lång och att det finns en instriven titel. Titeln på eventet blir den angivna
        titeln, startiden blir den dag/tid användaren valt och sluttid där användaren släppt/inmatat
        tid eller datum */
        
    })

});

$('#calendar').fullCalendar('next');
// för att komma till nästa vecka eller månad

$('#calendar').fullCalendar({
    navLinks: true,
    navLinkDayClick: function(date, jsEvent) {
        console.log('day', date.format()); // date is a moment
        console.log('coords', jsEvent.pageX, jsEvent.pageY);
    } // länkar siffran (dagens datum) i kalendern till specifika sidan för den dagen

});

                   