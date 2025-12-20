// @param src - The source URL of the image to be converted.
// @param onCanvas - Optional callback that receives the resulting canvas.
// @returns A 2D binary array representation of the image (contains only 0s and 1s).

import React, { useRef, useEffect } from "react";

/**
 * Convert an image (by URL) to a binary 2D array and provide the canvas via `onCanvas`.
 * The computed binary array is attached to the canvas as `__binary` (number[][]).
 */
function ConvertToBinary({
  src,
  onCanvas,
  onBinary,
}: {
  src: string;
  onCanvas?: (canvas: HTMLCanvasElement) => void;
  onBinary?: (binary: number[][]) => void;
}) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    if (!src) return;

    const img = new Image();
    img.crossOrigin = "Anonymous";
    let cancelled = false;

    const handleLoad = () => {
      if (cancelled) return;
      const canvas = canvasRef.current ?? document.createElement("canvas");
      const width = img.naturalWidth || img.width || 0;
      const height = img.naturalHeight || img.height || 0;
      if (!width || !height) return;
      canvas.width = width;
      canvas.height = height;

      const ctx = canvas.getContext("2d");
      if (!ctx) return;
      ctx.drawImage(img, 0, 0, width, height);

      try {
        const imgData = ctx.getImageData(0, 0, width, height);
        const data = imgData.data;
        const binary: number[][] = [];
        for (let y = 0; y < height; y++) {
          const row: number[] = [];
          for (let x = 0; x < width; x++) {
            const i = (y * width + x) * 4;
            const r = data[i];
            const g = data[i + 1];
            const b = data[i + 2];
            const l = 0.2126 * r + 0.7152 * g + 0.0722 * b; // luminance
            row.push(l >= 128 ? 1 : 0);
          }
          binary.push(row);
        }

        // Attach binary to canvas for consumers
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-ignore
        canvas.__binary = binary;
        onCanvas?.(canvas);
        onBinary?.(binary);
      } catch (e) {
        // Could be CORS or other canvas read issue — still provide canvas
        // eslint-disable-next-line no-console
        console.error("ConvertToBinary error:", e);
        onCanvas?.(canvas);
      }
    };

    const handleError = (ev: any) => {
      // eslint-disable-next-line no-console
      console.error("Failed to load image for ConvertToBinary:", ev);
    };

    img.addEventListener("load", handleLoad);
    img.addEventListener("error", handleError);
    img.src = src;

    return () => {
      cancelled = true;
      img.removeEventListener("load", handleLoad);
      img.removeEventListener("error", handleError);
    };
  }, [src, onCanvas, onBinary]);

  return onBinary;
}

export default ConvertToBinary;
