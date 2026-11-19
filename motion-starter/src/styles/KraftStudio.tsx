import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۰۴ — کرافت / کارگاه چوب (Kraft / Artisan)
 * کاغذ کرافت، زغالی، کارت تیره، حس دست‌ساز و گرم.
 * زبان بصری: کافه، قهوه، نان، محصول دست‌ساز، برند محلی.
 */

const KRAFT = "#C6A57A";
const CHARCOAL = "#2A2521";
const CREAM = "#F2E7D3";

export const KraftStudio: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const card = spring({ frame, fps, config: { damping: 16, mass: 1 } });
  const stamp = spring({ frame: frame - 30, fps, config: { damping: 9, mass: 0.7 } });

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at 30% 20%, #D6B98F 0%, ${KRAFT} 45%, #A9875C 100%)`,
        direction: "rtl",
        fontFamily: FONT,
        overflow: "hidden",
      }}
    >
      {/* بافت الیاف */}
      <AbsoluteFill
        style={{
          backgroundImage:
            "repeating-linear-gradient(93deg, rgba(90,65,35,0.06) 0px, rgba(90,65,35,0.06) 1px, transparent 1px, transparent 5px)",
        }}
      />

      <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
        <div
          style={{
            width: 1180,
            padding: "86px 92px",
            background: CHARCOAL,
            borderRadius: 18,
            boxShadow: "0 40px 90px rgba(40,25,10,0.45)",
            transform: `scale(${interpolate(card, [0, 1], [0.9, 1])}) rotate(${interpolate(card, [0, 1], [-1.5, 0])}deg)`,
            opacity: card,
            position: "relative",
            border: "1px solid rgba(242,231,211,0.16)",
          }}
        >
          {/* حاشیه‌ی خط‌چین */}
          <div style={{ position: "absolute", inset: 16, border: `1px dashed rgba(242,231,211,0.3)`, borderRadius: 10 }} />

          <div style={{ fontSize: 24, letterSpacing: 8, color: KRAFT, fontWeight: 700, direction: "ltr", marginBottom: 28 }}>
            HANDMADE · SINCE 2026
          </div>

          <div style={{ fontSize: 118, fontWeight: 900, color: CREAM, lineHeight: 1.22, letterSpacing: -1 }}>
            ایده، حرکت، ویدیو
          </div>

          <div style={{ fontSize: 32, color: "#C9BBA6", marginTop: 24, lineHeight: 1.7, fontWeight: 400 }}>
            ساخته‌شده با دست، رندر‌شده با کد.
          </div>

          {/* مهر */}
          <div
            style={{
              position: "absolute",
              left: 46,
              bottom: -34,
              width: 128,
              height: 128,
              borderRadius: "50%",
              border: `3px solid ${KRAFT}`,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              transform: `scale(${interpolate(stamp, [0, 1], [1.8, 1])}) rotate(${interpolate(stamp, [0, 1], [-30, -12])}deg)`,
              opacity: stamp,
              color: KRAFT,
              fontSize: 26,
              fontWeight: 900,
              textAlign: "center",
              lineHeight: 1.3,
            }}
          >
            اصل
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
