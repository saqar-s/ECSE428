import React, { useEffect } from "react";
import { COLORS, FONTS } from "../GLOBAL";

import FullCalendar from "@fullcalendar/react";
import timeGridPlugin from '@fullcalendar/timegrid';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';

const Calendar = () => {
    useEffect(() => {
        const calendarEl = document.getElementById('calendar');
        const calendar = new FullCalendar(calendarEl, {
            plugins: [dayGridPlugin, timeGridPlugin, interactionPlugin],
            initialView: 'timeGridWeek',
            headerToolbar: {
                left: 'prev,next today',
                center: 'Meal Planner Calendar',
                right: 'timeGridWeek,timeGridDay dayGridMonth'
            },
            editable: true,
            selectable: true,
            selectMirror: true,
            select: function (arg) {
                var title = prompt('Event Title:');
                if (title) {
                    calendar.addEvent({
                        title: title,
                        start: arg.start,
                        end: arg.end,
                        allDay: arg.allDay
                    })
                }
                calendar.unselect()
            },
            eventClick: function (info) {
                info.event.remove()
            },
            events: '/getCalendarEvents'
        });
    });
};
export default Calendar;