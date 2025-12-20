// @param 2d binary array
// @returns HTMLCanvasElement - The input image to convert

function ConvertToBinary(binaryArray: number[][]){

  const out = document.createElement("canvas");
  out.width = binaryArray[0].length;
  out.height = binaryArray.length;
  const outCtx = out.getContext("2d")!;

  const imageData = outCtx.getImageData(0, 0, out.width, out.height);
  const data = imageData.data;

//   let binaryArray: number[][] = [];

  for (let y = 0; y < out.height; y++) {
    for (let x = 0; x < out.width; x++) {
        data[(y * out.width + x) * 4] = binaryArray[y][x] === 1 ? 255 : 0;        // Red
        data[(y * out.width + x) * 4 + 1] = binaryArray[y][x] === 1 ? 255 : 0;    // Green
        data[(y * out.width + x) * 4 + 2] = binaryArray[y][x] === 1 ? 255 : 0;    // Blue
        data[(y * out.width + x) * 4 + 3] = 255;                                  // Alpha
    }
    }   
return imageData;

}
  

export default ConvertToBinary;
