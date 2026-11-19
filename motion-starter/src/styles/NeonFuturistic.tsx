import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۰۲ — نئون / سایبرپانک
 * پس‌زمینه‌ی مشکی-آبی، خطوط نئونی، درخشش (glow)، اسکن‌لاین، گلیچ خفیف.
 * زبان بصری: آینده، تکنولوژی، بازی، موسیقی الکترونیک.
 */

const GLOW = "#00F0FF";
const PINK = "#FF2E97";

export const NeonFuturistic: React.FC = () => {
  const frame = useCurrentFrame();
  const flicker = frame < 20 ? (Math.sin(frame * 3) > -0.2 ? 1 : 0.35) : 1;
  const glitch = frame > 55 && frame < 66 ? Math.sin(frame * 9) * 7 : 0;
  const grid = interpolate(frame, [0, 150], [0, 120]);
  const scan = (frame * 9) % 1200;

  return (
    <AbsoluteFill style={{ background: "#04060F", direction: "rtl", fontFamily: FONT, overflow: "hidden" }}>
      {/* شبکه‌ی پرسپکتیو */}
      <AbsoluteFill
        style={{
          backgroundImage: `linear-gradient(${GLOW}22 1px, transparent 1px), linear-gradient(90deg, ${GLOW}22 1px, transparent 1px)`,
          backgroundSize: "80px 80px",
          backgroundPosition: `0px ${grid}px`,
          transform: "perspective(600px) rotateX(48deg) scale(1.8)",
          transformOrigin: "center bottom",
          opacity: 0.55,
        }}
      />
      {/* هاله‌های نئونی */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse at 25% 30%, ${GLOW}30, transparent 45%), radial-gradient(ellipse at 78% 72%, ${PINK}2A, transparent 45%)`,
        }}
      />

      {/* خط اسکن */}
      <div style={{ position: "absolute", top: scan, left: 0, right: 0, height: 3, background: `${GLOW}66`, filter: "blur(1px)" }} />

      <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", flexDirection: "column" }}>
        <div style={{ fontSize: 26, letterSpacing: 14, color: GLOW, marginBottom: 30, direction: "ltr", opacity: flicker }}>
          ▮ SYSTEM ONLINE
        </div>

        <div
          style={{
            fontSize: 190,
            fontWeight: 900,
            color: "#fff",
            letterSpacing: -3,
            textShadow: `0 0 18px ${GLOW}, 0 0 60px ${GLOW}88, ${glitch}px 0 0 ${PINK}, ${-glitch}px 0 0 ${GLOW}`,
            transform: `translateX(${glitch}px)`,
          }}
        >
          ایده، حرکت
        </div>

        {/* خط زیر متن */}
        <div
          style={{
            height: 4,
            width: interpolate(frame, [18, 60], [0, 780], { extrapolateRight: "clamp", extrapolateLeft: "clamp" }),
            background: `linear-gradient(90deg, transparent, ${PINK}, ${GLOW}, transparent)`,
            boxShadow: `0 0 24px ${PINK}`,
            marginTop: 18,
          }}
        />

        <div style={{ fontSize: 34, color: "#9FB4CC", marginTop: 34, letterSpacing: 6, opacity: interpolate(frame, [40, 70], [0, 1], { extrapolateRight: "clamp", extrapolateLeft: "clamp" }) }}>
          نئون · سایبر · آینده
        </div>
      </AbsoluteFill>

      {/* اسکن‌لاین‌ها */}
      <AbsoluteFill
        style={{
          backgroundImage: "repeating-linear-gradient(0deg, rgba(0,0,0,0.35) 0px, rgba(0,0,0,0.35) 1px, transparent 1px, transparent 4px)",
          mixBlendMode: "multiply",
        }}
      />
    </AbsoluteFill>
  );
};
