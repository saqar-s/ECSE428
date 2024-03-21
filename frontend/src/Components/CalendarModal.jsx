import React from "react";
import {
    Modal,
    Box,
    DialogTitle,
    DialogContent,
    DialogActions,
} from "@mui/material";
import {
    CustomButton,
  } from "../Components";
// import FullCalendar from '@fullcalendar/react'
// import dayGridPlugin from '@fullcalendar/daygrid'
import { COLORS, FONTS } from "../GLOBAL";
import { addToCalendar } from "../APIcalls/CalendarCalls";

const CalendarModal = () => {
    const [open, setOpen] = React.useState(false);

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
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="scroll-dialog-title"
                aria-describedby="scroll-dialog-description"
                PaperProps={{
                    sx: {
                        borderRadius: 12,
                        backgroundColor: COLORS.PrimaryPink,
                        width: "70%",
                    },
                }}
            >
                <div
                    style={{
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    margin: 12,
                    }}
                >
                    <Box sx={{ borderRadius: 12,
                            backgroundColor: COLORS.PrimaryPink,
                            width: "70%",
                            }}>
                        <DialogTitle
                            id="scroll-dialog-title"
                            sx={{
                                fontFamily: FONTS.InriaSerif,
                                fontSize: "1.5vw",
                                fontWeight: "2.5vw",
                                textAlign: "center",
                                color: COLORS.Black,
                            }}
                        >
                            Which day of the week would you like to have this meal?
                        </DialogTitle>
                        {/* You can add your content here */}
                        
                    </Box>
                </div>
            </Modal>
        </div>
    );
};

export default CalendarModal;