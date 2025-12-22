import ProcessImage from "../components/ProcessImage";
import Upload from "../components/Upload";
import Box from "@mui/material/Box";
import box from "../types/box";
import { ThemeProvider } from "@mui/material";
import theme from "../types/theme";
import Grid from "@mui/material/Grid";
import BlackWhiteImage from "../components/BlackWhiteImage";
import React from "react";
import EncodeRepetition from "../components/repetition/EncodeRepetition";
import GenerateNoise from "../components/GenerateNoise";
// import ConvertToBinary from "../conversions/ConvertToBinary";
import AddNoise from "../components/AddNoise";
import DecodeRepetition from "../components/repetition/DecodeRepetition";

function Testing() {
  const [imageSrc, setImageSrc] = React.useState<string | null>(null);
  const [repetitionSrc, setRepetitionSrc] = React.useState<string | null>(null);
  const [noiseSrc, setNoiseSrc] = React.useState<string | null>(null);
  const [addedNoiseSrc, setAddedNoiseSrc] = React.useState<string | null>(null);
  const [decodedSrc, setDecodedSrc] = React.useState<string | null>(null);

  const setEncode = (
    canvas: HTMLCanvasElement | null
  ): HTMLCanvasElement | null => {
    try {
      let out = EncodeRepetition(canvas);
      setRepetitionSrc(out.toDataURL());
      return out;
    } catch (e) {
      setRepetitionSrc(null);
      return null;
    }
  };

  const setNoise = (
    canvas: HTMLCanvasElement | null,
    noiseAmount = 0.001
  ): HTMLCanvasElement | null => {
    try {
      let outNoise = GenerateNoise(canvas, noiseAmount);
      setNoiseSrc(outNoise.toDataURL());
      return outNoise;
    } catch (e) {
      setNoiseSrc(null);
      return null;
    }
  };

  const setAddNoise = (
    canvas: HTMLCanvasElement | null,
    canvas2: HTMLCanvasElement | null
  ) => {
    try {
      let outAddedNoise = AddNoise(canvas, canvas2);
      setAddedNoiseSrc(outAddedNoise.toDataURL());
      return outAddedNoise;
    } catch (e) {
      setAddedNoiseSrc(null);
      return null;
    }
  };

  const setDecode = (canvas: HTMLCanvasElement | null) => {
    try {
      let decodedImage = DecodeRepetition(canvas);
      setDecodedSrc(decodedImage.toDataURL());
      return decodedImage;
    } catch (e) {
      setDecodedSrc(null);
      return null;
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <Grid display="flex" justifyContent="center" alignItems="center">
        <Box sx={box}>
          <Upload onUpload={(src: string) => setImageSrc(src)} />

          {imageSrc && (
            <BlackWhiteImage
              src={imageSrc}
              onCanvas={(canvas) => {
                let encoded = setEncode(canvas);
                let outNoise = setNoise(encoded);
                let outAddedNoise = setAddNoise(encoded, outNoise);
                setDecode(outAddedNoise);
              }}
            />
          )}
          {repetitionSrc && (
            <Box sx={{ marginTop: 2 }}>
              <img
                src={repetitionSrc}
                alt="inverted"
                style={{ maxWidth: "100%" }}
              />
            </Box>
          )}
          {noiseSrc && (
            <Box sx={{ marginTop: 2 }}>
              <img src={noiseSrc} alt="inverted" style={{ maxWidth: "100%" }} />
            </Box>
          )}
          {addedNoiseSrc && (
            <Box sx={{ marginTop: 2 }}>
              <img
                src={addedNoiseSrc}
                alt="inverted"
                style={{ maxWidth: "100%" }}
              />
            </Box>
          )}
          {decodedSrc && (
            <Box sx={{ marginTop: 2 }}>
              <img
                src={decodedSrc}
                alt="inverted"
                style={{ maxWidth: "100%" }}
              />
            </Box>
          )}
        </Box>
      </Grid>
    </ThemeProvider>
  );
}

export default Testing;
