import React from "react";
import { AbsoluteFill, Easing, interpolate, useCurrentFrame } from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۱۰ — کلی/نرم سه‌بعدی (Claymorphism / Soft 3D)
 * حجم‌های پاستلی گرد، سایه‌های دوگانه (نور و بازتاب)، حس لمس‌پذیر.
 * زبان بصری: اپ موبایل، کودک، سلامت، فین‌تک دوستانه.
 */

const BG = "#EEF1FF";

const Blob: React.FC<{ x: number; y: number; size: number; color: string; r: number; delay: number; frame: number }> = ({ x, y, size, color, r, delay, frame }) => {
  const float = Math.sin((frame + delay) / 32) * 18;
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y + float,
        width: size,
        height: size,
        borderRadius: `${r}%`,
        background: color,
        boxShadow: `inset -14px -14px 34px rgba(120,110,180,0.28), inset 14px 14px 30px rgba(255,255,255,0.9), 22px 26px 50px rgba(110,110,170,0.22)`,
      }}
    />
  );
};

export const ClaySoft: React.FC = () => {
  const frame = useCurrentFrame();
  const cardIn = interpolate(frame, [0, 26], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.back(1.6)) });

  return (
    <AbsoluteFill style={{ background: BG, direction: "rtl", fontFamily: FONT, overflow: "hidden" }}>
      <AbsoluteFill style={{ background: "radial-gradient(ellipse at 15% 10%, #FFFFFF, transparent 55%)" }} />

      <Blob x={-70} y={-60} size={330} color="#C7B8FF" r={46} delay={0} frame={frame} />
      <Blob x={1560} y={120} size={230} color="#9EE6D0" r={52} delay={40} frame={frame} />
      <Blob x={120} y={760} size={260} color="#FFC9D8" r={48} delay={70} frame={frame} />
      <Blob x={1480} y={700} size={190} color="#FFE2A8" r={44} delay={90} frame={frame} />

      <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
        <div
          style={{
            transform: `scale(${cardIn})`,
            opacity: Math.min(1, cardIn * 1.4),
            padding: "86px 104px",
            borderRadius: 70,
            background: "#F7F9FF",
            boxShadow: "inset -18px -18px 44px rgba(140,150,200,0.25), inset 18px 18px 40px rgba(255,255,255,1), 30px 40px 80px rgba(120,125,180,0.25)",
            textAlign: "center",
          }}
        >
          <div style={{ fontSize: 30, letterSpacing: 10, color: "#8E94BE", fontWeight: 700, marginBottom: 26, direction: "ltr" }}>
            SOFT · 3D
          </div>
          <div style={{ fontSize: 124, fontWeight: 900, color: "#3A3F63", lineHeight: 1.16, letterSpacing: -2 }}>
            ایده، حرکت، ویدیو
          </div>
          <div style={{ display: "flex", gap: 20, justifyContent: "center", marginTop: 46 }}>
            {["#C7B8FF", "#9EE6D0", "#FFC9D8"].map((c, i) => (
              <div
                key={c}
                style={{
                  width: 84,
                  height: 84,
                  borderRadius: "50%",
                  background: c,
                  boxShadow: "inset -6px -6px 16px rgba(120,110,180,0.3), inset 6px 6px 14px rgba(255,255,255,0.95), 8px 10px 22px rgba(120,125,180,0.25)",
                  transform: `translateY(${Math.sin((frame + i * 14) / 22) * 8}px)`,
                }}
              />
            ))}
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
