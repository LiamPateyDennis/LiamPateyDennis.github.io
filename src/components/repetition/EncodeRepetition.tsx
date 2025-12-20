function EncodeRepetition(image: HTMLCanvasElement | null): HTMLCanvasElement {
  let srcCanvas: HTMLCanvasElement;

  if (image instanceof HTMLCanvasElement) {
    srcCanvas = image;
  } else {
    throw new Error("No image provided to EncodeRepetition");
  }

  const tileX = 3;
  const tileY = 1;
  const out = document.createElement("canvas");
  out.width = srcCanvas.width * tileX;
  out.height = srcCanvas.height * tileY;
  const outCtx = out.getContext("2d")!;

  for (let y = 0; y < tileY; y++) {
    for (let x = 0; x < tileX; x++) {
      outCtx.drawImage(srcCanvas, x * srcCanvas.width, y * srcCanvas.height);
    }
  }

  return out;
}

export default EncodeRepetition;
