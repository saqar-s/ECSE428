import React from "react";

import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
  Calendar,
} from "../Components";
import { COLORS, FONTS } from "../GLOBAL";
import { Dialog, DialogContent, DialogTitle } from "@mui/material";
import { addToCalendar } from "../APIcalls/CalendarCalls";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import { DateCalendar } from "@mui/x-date-pickers/DateCalendar";

const CalendarScreen = () => {
  const [dialogOpen, setDialogOpen] = React.useState(false);
  const handleCLose = (reason) => {
    if (reason === "clickaway") {
      return;
    }
    setDialogOpen(false);
  };
  return <div></div>;
};

export default CalendarScreen;
