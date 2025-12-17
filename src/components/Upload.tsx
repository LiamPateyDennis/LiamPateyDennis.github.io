import { styled } from "@mui/material/styles";
import Button from "@mui/material/Button";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";

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

interface InputFileUploadProps {
  onUpload: (src: string) => void;
}

export default function InputFileUpload({ onUpload }: InputFileUploadProps) {
  return (
    <Button
      component="label"
      role={undefined}
      variant="contained"
      tabIndex={-1}
      startIcon={<CloudUploadIcon />}
      // sx={border: "2px dashed grey", padding: "20px"}
    >
      Upload file
      <VisuallyHiddenInput
        type="file"
        onChange={(event) => {
          const file = event.target.files?.[0];
          if (file) {
            const src = URL.createObjectURL(file);
            onUpload(src);
          }
        }}
      />
    </Button>
  );
}
