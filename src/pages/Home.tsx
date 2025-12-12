import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import { Typography } from "@mui/material";
import theme from "../types/theme";
import { ThemeProvider } from "@mui/material";
import { Grid } from "@mui/material";
import { motion } from "motion/react";
import AlbumIcon from "@mui/icons-material/Album";
import ComputerIcon from "@mui/icons-material/Computer";
import SendBinAnimation from "../components/SendBinAnimation";

const box = {
  width: 100,
  height: 100,
  backgroundColor: "#ff0088",
  borderRadius: 5,
};

function Home() {
  return (
    <ThemeProvider theme={theme}>
      <Grid
        display="flex"
        justifyContent="center"
        alignItems="center"
        size="grow"
      >
        <Box
          component="section"
          sx={{
            p: 3,
            typography: "body1",
            width: 800,
            borderRadius: 5,
            border: "1px dashed white",
            bgcolor: "primary.dark",
            mt: 5,
          }}
        >
          <Box
            sx={{
              color: "primary.contrastText",
              fontSize: 15,
              fontWeight: 200,
              fontFamily: "monospace",
            }}
          >
            The quality of a message depends entirely on the strength of the
            signal received. In the early 1940s, Richard Hamming confronted this
            challenge while working at Bell Labs. There, he had access to the
            relay-based Bell Model V Computer, a machine used for complex
            engineering calculations that often ran unattended over weekends.
            Frustrated by the frequent errors it produced, Hamming set out to
            develop a method that could not only detect mistakes but also
            automatically correct them. A method now referred to as Forward
            Error Correction (FEC).
          </Box>
          <br />
          <Grid
            container
            spacing={2}
            display="flex"
            justifyContent="center"
            alignItems="center"
            size="grow"
          >
            <Grid
              size={2}
              display="flex"
              justifyContent="center"
              alignItems="center"
            >
              <AlbumIcon sx={{ color: "primary.contrastText", fontSize: 60 }} />
            </Grid>
            <Grid
              size={8}
              display="flex"
              justifyContent="center"
              alignItems="center"
            >
              <SendBinAnimation />
            </Grid>
            <Grid
              size={2}
              display="flex"
              justifyContent="center"
              alignItems="center"
            >
              <ComputerIcon
                sx={{ color: "primary.contrastText", fontSize: 60 }}
              />
            </Grid>
          </Grid>
          <br />
          <Box
            sx={{
              color: "primary.contrastText",
              fontSize: 15,
              fontWeight: 200,
              fontFamily: "monospace",
            }}
          >
            The most common example of FEC, is the CD. The CD is encoded using
            the Reed Solomon Codes. When the CD is scratched, binary on the disk
            is changed. However, the original message, a movie or video game, is
            still mostly intact. So how does it do that?
          </Box>
        </Box>
      </Grid>
    </ThemeProvider>
  );
}

export default Home;
