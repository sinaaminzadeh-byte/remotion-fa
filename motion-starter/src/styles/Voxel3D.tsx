import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۰۶ — وکسل / ایزومتریک سه‌بعدی (Voxel / Isometric)
 * مکعب‌های ایزومتریک، پاستل، عمق واقعی با CSS 3D.
 * زبان بصری: بازی، آموزش، تکنولوژی دوستانه، محتوای گیک.
 */

const CUBES = [
  { x: 200, y: 300, size: 130, color: "#6C5CE7", delay: 0 },
  { x: 1490, y: 220, size: 100, color: "#00B894", delay: 8 },
  { x: 1650, y: 640, size: 150, color: "#FDCB6E", delay: 16 },
  { x: 300, y: 800, size: 110, color: "#E17055", delay: 24 },
  { x: 1200, y: 860, size: 90, color: "#0984E3", delay: 32 },
];

const Cube: React.FC<{ x: number; y: number; size: number; color: string; delay: number; frame: number }> = ({ x, y, size, color, delay, frame }) => {
  const float = Math.sin((frame + delay * 4) / 26) * 16;
  const spin = frame * 0.35 + delay * 12;
  const h = size / 2;
  return (
    <div style={{ position: "absolute", left: x, top: y + float, width: size, height: size, transformStyle: "preserve-3d", transform: `rotateX(-24deg) rotateY(${spin}deg)` }}>
      {[
        { t: `translateZ(${h}px)`, c: color, o: 1 },
        { t: `rotateY(90deg) translateZ(${h}px)`, c: color, o: 0.7 },
        { t: `rotateY(-90deg) translateZ(${h}px)`, c: color, o: 0.82 },
        { t: `rotateX(90deg) translateZ(${h}px)`, c: color, o: 0.5 },
        { t: `rotateX(-90deg) translateZ(${h}px)`, c: color, o: 0.6 },
        { t: `rotateY(180deg) translateZ(${h}px)`, c: color, o: 0.62 },
      ].map((f, i) => (
        <div
          key={i}
          style={{
            position: "absolute",
            width: size,
            height: size,
            background: f.c,
            opacity: f.o,
            border: "2px solid rgba(255,255,255,0.55)",
            borderRadius: 10,
            boxShadow: "inset 0 0 40px rgba(0,0,0,0.18)",
            transform: f.t,
          }}
        />
      ))}
    </div>
  );
};

export const Voxel3D: React.FC = () => {
  const frame = useCurrentFrame();
  const title = interpolate(frame, [10, 36], [0, 1], { extrapolateRight: "clamp", extrapolateLeft: "clamp" });

  return (
    <AbsoluteFill style={{ background: "linear-gradient(170deg, #EAF7F1 0%, #D9E9FF 100%)", direction: "rtl", fontFamily: FONT, overflow: "hidden", perspective: 1200 }}>
      {CUBES.map((c, i) => (
        <Cube key={i} {...c} frame={frame} />
      ))}

      <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
        <div
          style={{
            opacity: title,
            transform: `translateY(${interpolate(title, [0, 1], [40, 0])}px)`,
            textAlign: "center",
          }}
        >
          <div
            style={{
              fontSize: 150,
              fontWeight: 900,
              color: "#2D3436",
              letterSpacing: -2,
              textShadow: "6px 6px 0 #fff, 12px 12px 0 rgba(108,92,231,0.35)",
            }}
          >
            ایده، حرکت
          </div>
          <div style={{ fontSize: 32, color: "#5A6772", marginTop: 44, letterSpacing: 8, fontWeight: 700, direction: "ltr" }}>
            ISOMETRIC · VOXEL
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
