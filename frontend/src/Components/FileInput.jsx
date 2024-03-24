import React, { useState } from "react";
import { FormLabel, Button, Typography, styled } from "@mui/material";
import { COLORS, FONTS } from "../GLOBAL";
import AddAPhotoIcon from "@mui/icons-material/AddAPhoto";

const FileInput = ({
  label,
  helpertext,
  hasError,
  onClick,
  style,

  width = "50%",
}) => {
  const [isUploaded, setUploaded] = useState(false);
  const [error, setError] = useState("");
  const [fileReader, setFileReader] = useState("");

  let file;
  const handleFileChange = (event) => {
    file = event.target.files[0];
    const reader = new FileReader();
    reader.onloadend = () => {
      setUploaded(true);
      setFileReader(reader.result);
    };
    reader.readAsDataURL(file);

    setUploaded(true);
    const allowedTypes = ["image/jpeg", "image/png", "image/gif"];

    if (file && allowedTypes.includes(file.type)) {
      if (onClick && typeof onClick === "function") {
        onClick(file);
      }
      setError("");
    } else {
      event.target.value = null;

      setError("Please choose a valid image file (JPEG, PNG, GIF).");
    }
  };
  const VisuallyHiddenInput = styled("input")({
    clip: "rect(0 0 0 0)",
    clipPath: "inset(50%)",
    height: 1,
    overflow: "hidden",
    position: "absolute",
    bottom: 0,
    left: 0,
    whiteSpace: "nowrap",
    width: 1,
  });
  return (
    <>
      <FormLabel
        sx={{
          color: COLORS.White,
          fontFamily: FONTS.InriaSerif,
          fontSize: 16,
          marginBottom: 0.5,
        }}
        helpertext={error}
      >
        {label}
      </FormLabel>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          height: "100px",
          margin: 6,
        }}
      >
        <Button
          sx={{
            background: isUploaded ? `url(${fileReader})` : COLORS.White,
            backgroundSize: "cover",
            backgroundPosition: "center",
            borderRadius: 6,
            width: "200px",
            textTransform: "none",
            "&:hover": isUploaded ? `url(${fileReader})` : COLORS.White,
          }}
          component="label"
        >
          <VisuallyHiddenInput type="file" onChange={handleFileChange} />

          <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <>
              <AddAPhotoIcon
                sx={{
                  color: COLORS.Black,
                  opacity: isUploaded ? 1 : 0.6,
                  fontSize: 34,
                }}
              />
              <Typography
                color={COLORS.Black}
                fontSize={16}
                textTransform={"none"}
                fontFamily={FONTS.InriaSerif}
                sx={{ opacity: isUploaded ? 1 : 0.6 }}
              >
                {isUploaded
                  ? "Click to change photo"
                  : "Click to upload a photo"}
              </Typography>
            </>
          </div>
        </Button>
      </div>
    </>
  );
};

export default FileInput;
