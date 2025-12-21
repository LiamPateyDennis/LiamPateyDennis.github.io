import ConvertToBinary from "../../conversions/ConvertToBinary";
import ConvertToImage from "../../conversions/ConvertToImage";

function DecodeRepetition(image: HTMLCanvasElement | null): HTMLCanvasElement {
  let srcCanvas: HTMLCanvasElement;

  if (image instanceof HTMLCanvasElement) {
    srcCanvas = image;
  } else {
    throw new Error("No image provided to DecodeRepetition");
  }

  const binaryArray = ConvertToBinary(srcCanvas);
  const unitWidth = srcCanvas.width / 3;

  for (let y = 0; y < srcCanvas.height; y++) {
    for (let x = 0; x < unitWidth; x++) {
      if (
        (binaryArray[y][x] +
          binaryArray[y][x + unitWidth] +
          binaryArray[y][x + 2 * unitWidth]) %
          3 !==
        0
      ) {
        (binaryArray[y][x] +
          binaryArray[y][x + unitWidth] +
          binaryArray[y][x + 2 * unitWidth]) %
          3 ===
        1
          ? (binaryArray[y][x] =
              binaryArray[y][x + unitWidth] =
              binaryArray[y][x + 2 * unitWidth] =
                0)
          : (binaryArray[y][x] =
              binaryArray[y][x + unitWidth] =
              binaryArray[y][x + 2 * unitWidth] =
                1);
      }
    }
  }

  // & - bitwise AND, 0 & 0 = 0, 0 & 1 = 0, 1 & 0 = 0, 1 & 1 = 1
  // && - logical AND, if this and this do that

  const out = ConvertToImage(binaryArray);
  return out;
}

export default DecodeRepetition;
