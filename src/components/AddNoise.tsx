import ConvertToBinary from "../conversions/ConvertToBinary";
import ConvertToImage from "../conversions/ConvertToImage";

// @param HTMLCanvasElement - The input image to add noise to
// @param HTMLCanvasElement - The noise image to add
// @returns HTMLCanvasElement - Returns a new image of the input image and noise combined.

function AddNoise(
  image: HTMLCanvasElement | null,
  image2: HTMLCanvasElement | null
) {
  if (image === null || image2 === null) {
    throw new Error("Missing image provided to AddNoise");
  }

  const binaryArray = ConvertToBinary(image);
  const noiseArray = ConvertToBinary(image2);

  for (let y = 0; y < image.height; y++) {
    for (let x = 0; x < image.width; x++) {
      if (noiseArray[y][x] === 1) {
        binaryArray[y][x] = binaryArray[y][x] === 1 ? 0 : 1;
      }
    }
  }

  const out = ConvertToImage(binaryArray);
  return out;
}

export default AddNoise;
