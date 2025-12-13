import { motion } from "motion/react";

function SendBinAnimation() {
  const text = "1 0 1 1 0 1 0 0 1 0 1 1 0 0 0 1 0 1 1 1 0 1";
  const Duration = 25;

  return (
    <div
      style={{
        width: "550px",
        height: "20px",
        overflow: "hidden",
        // border: "2px solid #333",
        position: "relative",
        whiteSpace: "nowrap",
        color: "lime",
        fontFamily: "monospace",
        alignContent: "inherit",
      }}
    >
      {/* First strip */}
      <motion.div
        animate={{ x: ["-100%", "0%"] }}
        transition={{
          repeat: Infinity,
          duration: Duration,
          ease: "linear",
        }}
        style={{
          display: "inline-block",
          position: "absolute",
          //   alignItems: "center",
          //   justifyContent: "center",
          alignContent: "inherit",
        }}
      >
        <span>{text}&nbsp;</span>
        <span>{text}&nbsp;</span>
        <span>{text}&nbsp;</span>
      </motion.div>
      {/* Second strip, offset so it follows immediately */}
      <motion.div
        animate={{ x: ["0%", "100%"] }}
        transition={{
          repeat: Infinity,
          duration: Duration,
          ease: "linear",
        }}
        style={{
          display: "inline-block",
          position: "absolute",
          alignContent: "inherit",
        }}
      >
        <span>{text}&nbsp;</span>
        <span>{text}&nbsp;</span>
        <span>{text}&nbsp;</span>
      </motion.div>
    </div>
  );
}

export default SendBinAnimation;
