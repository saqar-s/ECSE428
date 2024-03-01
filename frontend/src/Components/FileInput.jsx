import React, { useState } from "react";
import {
  FormControl,
  FormLabel,
  Button,
  Typography,
} from "@mui/material";
import { COLORS, FONTS } from "../GLOBAL";

const FileInput = ({
  label,
  text,
  helpertext,
  hasError,
  onClick,
  style,
  inputHeight = "50px",
  isMultiline = false,
  width = "50%",
  labelColor = COLORS.Black,
}) => {
  const [fileName, setFileName] = useState("");
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    const allowedTypes = ["image/jpeg", "image/png", "image/gif"];

    if (file && allowedTypes.includes(file.type)) {
      setFileName(file.name);
      if (onClick && typeof onClick === "function") {
        onClick(file);
      }
      setError(""); // Clear any previous error message
    } else {
      // Reset the file input and display an error message
      event.target.value = null;
      setFileName("");
      setError("Please choose a valid image file (JPEG, PNG, GIF).");
    }
  };

  return (
    <FormControl sx={{ width: width, ...style }}>
      <FormLabel
        sx={{
          color: labelColor,
          fontFamily: FONTS.InriaSerif,
          fontSize: 16,
          marginBottom: 0.5,
        }}
      >
        {label}
      </FormLabel>
      <input
        type="file"
        id="file-input"
        style={{ display: "none" }}
        onChange={handleFileChange}
      />
      <Button 
        component="label"
        htmlFor="file-input"
        sx = {{
          backgroundColor: COLORS.White,
          borderRadius: 4,
          color: COLORS.Black,
          textTransform: "none",
          "&:hover": { background: COLORS.PrimaryPink, border: "1px solid #000000",},
          height: isMultiline ? "auto" : inputHeight,
        }}
      >
        {fileName ? fileName : "Choose File"}
      </Button>
      {error && (
        <Typography variant="caption" sx={{ color: "red" }}>
          {error}
        </Typography>
      )}
      {hasError && (
        <Typography variant="caption" sx={{ color: "red" }}>
          {helpertext}
        </Typography>
      )}
    </FormControl>
  );
};

export default FileInput;
