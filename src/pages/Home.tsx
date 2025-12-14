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
import box from "../types/box";
import heading from "../types/heading";
import text from "../types/text";

function Home() {
  return (
    <ThemeProvider theme={theme}>
      <Grid
        display="flex"
        justifyContent="center"
        alignItems="center"
        size="grow"
      >
        <Box component="section" sx={box}>
          <Box sx={heading}>What is this website?</Box>
          <Box sx={text}>
            The aim of this website is to show, mathematically and through
            interactive examples, the different kinds of Error Correcting Codes
            available to use.
          </Box>
          <br />
          <Grid
            container
            spacing={2}
            // display="flex"
            justifyContent="center"
            alignItems="center"
            size="grow"
          >
            <Grid
              size={1}
              display="flex"
              justifyContent="right"
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
              size={1}
              display="flex"
              justifyContent="left"
              alignItems="center"
            >
              <ComputerIcon
                sx={{ color: "primary.contrastText", fontSize: 60 }}
              />
            </Grid>
          </Grid>
          <br />
          <Box sx={text}>
            The most common example of an Error Correcting Code, is the CD. The
            CD is encoded using a Reed Solomon Code. When the CD is scratched,
            binary on the disk is changed. However, the original message, a
            movie or video game, is still mostly intact.
          </Box>
          <Box sx={heading}>
            <br />
            Origins
          </Box>
          <Box sx={text}>
            In the early 1940s, Richard Hamming confronted a challenge while
            working at Bell Labs. There, he had access to the relay-based Bell
            Model V Computer, a machine used for complex engineering
            calculations that often ran unattended over weekends. Frustrated by
            the frequent errors it produced, Hamming set out to develop a method
            that could not only detect mistakes but also automatically correct
            them. A method now referred to as Forward Error Correction (FEC).
          </Box>
        </Box>
      </Grid>
    </ThemeProvider>
  );
}

export default Home;
