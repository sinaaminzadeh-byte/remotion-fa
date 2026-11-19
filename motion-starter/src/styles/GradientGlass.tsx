import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک ۲ — «گرادیان + شیشه» (Gradient / Glassmorphism)
 * پس‌زمینه‌ی گرادیانی متحرک، کارت شیشه‌ای با بلور، ورود نرم و مدرن.
 * مناسب: معرفی محصول، پست شبکه‌های اجتماعی، استارتاپ، SaaS.
 */

const CHIPS = ["ایده", "حرکت", "ویدیو"];

export const GradientGlass: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const a = interpolate(frame, [0, 150], [0, 45]);
  const b = interpolate(frame, [0, 150], [100, 65]);

  const card = spring({ frame, fps, config: { damping: 200, mass: 1.1 } });
  const cardY = interpolate(card, [0, 1], [70, 0]);
  const cardScale = interpolate(card, [0, 1], [0.94, 1]);

  return (
    <AbsoluteFill
      style={{
        direction: "rtl",
        background: `linear-gradient(${a + 120}deg, #1B1B4B 0%, #3B2E8F ${b / 2}%, #7A3FD4 ${b}%, #E2568C 100%)`,
      }}
    >
      {/* دو لکه‌ی نوری شناور */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at ${20 + Math.sin(frame / 30) * 8}% ${30 + Math.cos(frame / 40) * 10}%, rgba(120,220,255,0.55), transparent 42%)`,
          filter: "blur(20px)",
        }}
      />
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at ${78 + Math.cos(frame / 35) * 6}% ${72 + Math.sin(frame / 25) * 8}%, rgba(255,190,120,0.45), transparent 40%)`,
          filter: "blur(24px)",
        }}
      />

      <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
        <div
          style={{
            transform: `translateY(${cardY}px) scale(${cardScale})`,
            width: 1180,
            padding: "74px 84px",
            borderRadius: 44,
            background: "rgba(255,255,255,0.12)",
            border: "1px solid rgba(255,255,255,0.35)",
            boxShadow: "0 40px 120px rgba(20,10,60,0.45), inset 0 1px 0 rgba(255,255,255,0.5)",
            backdropFilter: "blur(26px)",
            WebkitBackdropFilter: "blur(26px)",
            fontFamily: FONT,
            color: "#fff",
            textAlign: "right",
          }}
        >
          <div style={{ fontSize: 26, letterSpacing: 8, opacity: 0.75, marginBottom: 26, direction: "ltr", textAlign: "left" }}>
            MOTION · 5s
          </div>
          <div style={{ fontSize: 104, fontWeight: 900, lineHeight: 1.15, letterSpacing: -2 }}>
            اولین موشن‌گرافیکت
          </div>
          <div style={{ fontSize: 38, fontWeight: 400, opacity: 0.85, marginTop: 18 }}>
            سه قدم ساده: ایده، حرکت، ویدیو.
          </div>

          <div style={{ display: "flex", gap: 18, marginTop: 44, justifyContent: "flex-start", flexDirection: "row" }}>
            {CHIPS.map((chip, i) => {
              const s = spring({ frame: frame - 26 - i * 9, fps, config: { damping: 14, mass: 0.5 } });
              return (
                <div
                  key={chip}
                  style={{
                    transform: `translateY(${interpolate(s, [0, 1], [26, 0])}px)`,
                    opacity: s,
                    padding: "16px 34px",
                    borderRadius: 999,
                    background: "rgba(255,255,255,0.22)",
                    border: "1px solid rgba(255,255,255,0.4)",
                    fontSize: 32,
                    fontWeight: 700,
                  }}
                >
                  {chip}
                </div>
              );
            })}
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
