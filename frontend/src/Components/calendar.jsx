import React from "react";
import { Dialog, DialogContent, DialogTitle } from "@mui/material";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { DateCalendar } from "@mui/x-date-pickers/DateCalendar";
import { COLORS, FONTS } from "../GLOBAL";
import CustomButton from "./CustomButton";
import { addToCalendar } from "../APIcalls/CalendarCalls";

const Calendar = ({ open, onClose, onSelect, recipeName }) => {
  const [selectedDate, setSelectedDate] = React.useState(null);
  const email = localStorage.getItem("username");
  console.log(email);
  const handleClose = (reason) => {
    if (reason === "clickaway") {
      return;
    }
    onClose();
  };

  const handleSave = async () => {
    if (selectedDate) {
      const data = {
        date: selectedDate.toISOString().split("T")[0],
        email: email,
        name: recipeName,
      };
      console.log(data);

      const response = await addToCalendar(data);

      console.log(response.message);
    }
  };
  return (
    <Dialog
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
      <DialogTitle
        id="scroll-dialog-title"
        alignSelf="center"
        sx={{
          fontFamily: FONTS.InriaSerif,
          fontSize: "1.5vw",
          fontWeight: "2.5vw",
          color: COLORS.White,
        }}
      >
        Which day of the week would you like to have this meal?
      </DialogTitle>
      <DialogContent dividers>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
          <DateCalendar
            onChange={(date) => setSelectedDate(date)}
            renderInput={(props) => <div {...props} />} // Render input field for accessibility
          />
        </LocalizationProvider>
        <div style={{ display: "flex", justifyContent: "center" }}>
          <CustomButton
            backgroundColor={COLORS.primaryBlue}
            label={"Save"}
            onClick={handleSave}
          />
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default Calendar;
