import React, { useRef, useEffect } from "react";

function BlackWhiteImage({
  src,
  onCanvas,
}: {
  src: string;
  onCanvas?: (canvas: HTMLCanvasElement) => void;
}) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const img = new Image();
    img.crossOrigin = "Anonymous";
    img.src = src;

    img.onload = () => {
      // Desired max size
      const maxWidth = 300;
      const maxHeight = 200;

      // Scale proportionally
      let { width, height } = img;
      const scale = Math.min(maxWidth / width, maxHeight / height);

      width *= scale;
      height *= scale;

      canvas.width = width;
      canvas.height = height;

      ctx.drawImage(img, 0, 0, width, height);

      const imageData = ctx.getImageData(0, 0, width, height);
      const data = imageData.data;

      for (let i = 0; i < data.length; i += 4) {
        const r = data[i];
        const g = data[i + 1];
        const b = data[i + 2];
        const luminance = 0.299 * r + 0.587 * g + 0.114 * b;
        const bw = luminance >= 128 ? 255 : 0;
        data[i] = data[i + 1] = data[i + 2] = bw;
      }

      ctx.putImageData(imageData, 0, 0);

      if (typeof onCanvas === "function") onCanvas(canvas);
    };
  }, [src]);

  return <canvas ref={canvasRef} style={{ maxWidth: "100%" }} />;
}

export default BlackWhiteImage;
