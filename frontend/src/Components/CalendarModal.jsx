import React from "react";
import {
    DialogTitle,
    DialogContent,
    DialogActions,
    Dialog,
} from "@mui/material";
import {
    CustomButton,
  } from "../Components";
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from "@fullcalendar/interaction"
import { COLORS, FONTS } from "../GLOBAL";
import { addToCalendar } from "../APIcalls/CalendarCalls";
import '@fullcalendar/common/main.css';
import "../Styles/calendar.css";


const CalendarModal = () => {
    const [open, setOpen] = React.useState(false);

    const handleDateClick = async (arg) => {
        console.log('Date clicked:', arg.dateStr);
        console.log(localStorage.getItem("username"))
        const recipeName = localStorage.getItem("recipeName"); //fix this
        const dateStr = arg.dateStr;
        const email = localStorage.getItem("username"); // Replace with actual user email

        try {
            const data = {
                email: email,
                recipeName: recipeName,
                date: dateStr,
            };
            const result = await addToCalendar(data);
            console.log(result);
            if (result && result.status === 201) {
                setOpen(false);
            } else {
                console.log("Failed to add to calendar");
            }
        }catch (error) {
            console.error(error);
          }
    };
    const handleOpen = () => {
        setOpen(true);
    };

    const handleClose = (reason) => {
        if (reason === "clickaway") {
          return;
        }
        setOpen(false);
    };

    return (
        <div>
            <CustomButton
                label={"Add to Calendar"}
                style={{ width: "10%" }}
                onClick={handleOpen}
            />
            {open && (
                <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby="scroll-dialog-title"
                PaperProps={{
                    sx: {
                    borderRadius: 12,
                    backgroundColor: COLORS.PrimaryPink,
                    width: "70%",
                    height: "90%",
                    },
                }}
                >
            <DialogTitle
                id="scroll-dialog-title"
                alignSelf={"center"}
                sx={{
                fontFamily: FONTS.InriaSerif,
                fontSize: "1.5vw",
                fontWeight: "2.5vw",
                color: COLORS.Black,
                }}
            >
                Which day of the week would you like to have this meal?
            </DialogTitle>
            <DialogContent>
                {/* <div
                    style={{
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    margin:12,
                    }}
                > */}
                    
                    <FullCalendar
                        plugins={[ dayGridPlugin, interactionPlugin]}
                        select={(arg) => handleDateClick(arg)}
                        initialView="dayGridMonth"
                        weekends={true}
                        className="calendar-container"
                        height="auto"
                        contentHeight="auto"
                        width="auto"
                        contentWidth="auto"
                        headerToolbar={{
                            start: "prev",
                            center: "title", // Center the month title
                            end: "next",
                        }}
                        themeSystem="standard"
                        
                    />
                
                {/* </div> */}
            </DialogContent>
            </Dialog>
            )}
        </div>
    );
};

export default CalendarModal;