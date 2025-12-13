import Box from "@mui/material/Box";
import theme from "../types/theme";
import { ThemeProvider } from "@mui/material";
import Grid from "@mui/material/Grid";
import text from "../types/text";
import box from "../types/box";
import heading from "../types/heading";

function Repetition() {
  return (
    <ThemeProvider theme={theme}>
      <Grid
        display="flex"
        justifyContent="center"
        alignItems="center"
        size="grow"
      >
        <Box component="section" sx={box}>
          <Box sx={heading}>Repetition</Box>
          <Box sx={text}>
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
        </Box>
      </Grid>
    </ThemeProvider>
  );
}

export default Repetition;
