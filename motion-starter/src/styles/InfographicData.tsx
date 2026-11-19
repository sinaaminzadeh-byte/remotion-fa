import React from "react";
import { AbsoluteFill, Easing, interpolate, useCurrentFrame } from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۰۸ — اینفوگرافیک / داده‌محور
 * نمودار میله‌ای و حلقه‌ای متحرک، اعداد شمارشی، شبکه‌ی خطوط ظریف.
 * زبان بصری: گزارش، آموزش، خبر، B2B، اعتمادآفرین.
 */

const BG = "#0E1526";
const CARD = "rgba(255,255,255,0.045)";
const CYAN = "#38E1C4";
const AMBER = "#FFB020";
const BARS = [
  { label: "ایده", value: 92 },
  { label: "حرکت", value: 76 },
  { label: "ویدیو", value: 64 },
  { label: "رندر", value: 88 },
];

const Ring: React.FC<{ p: number }> = ({ p }) => {
  const r = 92;
  const c = 2 * Math.PI * r;
  return (
    <svg width="220" height="220" style={{ transform: "rotate(-90deg)" }}>
      <circle cx="110" cy="110" r={r} fill="none" stroke="rgba(255,255,255,0.12)" strokeWidth="14" />
      <circle
        cx="110"
        cy="110"
        r={r}
        fill="none"
        stroke={AMBER}
        strokeWidth="14"
        strokeLinecap="round"
        strokeDasharray={c}
        strokeDashoffset={c * (1 - p)}
      />
    </svg>
  );
};

export const InfographicData: React.FC = () => {
  const frame = useCurrentFrame();
  const grow = interpolate(frame, [8, 70], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  const ringP = interpolate(frame, [20, 80], [0, 0.78], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  const count = Math.round(interpolate(frame, [20, 80], [0, 78], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }));
  const head = interpolate(frame, [0, 24], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ background: BG, direction: "rtl", fontFamily: FONT, overflow: "hidden" }}>
      {/* شبکه‌ی ظریف */}
      <AbsoluteFill
        style={{
          backgroundImage: "linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px)",
          backgroundSize: "72px 72px",
        }}
      />
      <AbsoluteFill style={{ background: `radial-gradient(ellipse at 70% 15%, ${CYAN}18, transparent 55%)` }} />

      <AbsoluteFill style={{ padding: "86px 104px" }}>
        <div style={{ opacity: head, transform: `translateY(${interpolate(head, [0, 1], [-20, 0])}px)` }}>
          <div style={{ fontSize: 26, letterSpacing: 8, color: CYAN, fontWeight: 700, direction: "ltr" }}>MOTION REPORT · 2026</div>
          <div style={{ fontSize: 76, fontWeight: 900, color: "#fff", marginTop: 14, letterSpacing: -1 }}>
            ایده، حرکت، ویدیو
          </div>
        </div>

        <div style={{ display: "flex", gap: 40, flex: 1, alignItems: "center", marginTop: 30 }}>
          {/* کارت نمودار میله‌ای */}
          <div style={{ flex: 1.4, background: CARD, border: "1px solid rgba(255,255,255,0.1)", borderRadius: 24, padding: "40px 48px" }}>
            <div style={{ display: "flex", flexDirection: "column", gap: 34 }}>
              {BARS.map((b, i) => {
                const bi = interpolate(grow, [i * 0.12, i * 0.12 + 0.55], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
                return (
                  <div key={b.label}>
                    <div style={{ display: "flex", justifyContent: "space-between", color: "#C8D3E4", fontSize: 26, marginBottom: 10 }}>
                      <span>{b.label}</span>
                      <span style={{ color: i % 2 ? AMBER : CYAN, fontWeight: 900, direction: "ltr" }}>{Math.round(b.value * bi)}%</span>
                    </div>
                    <div style={{ height: 16, background: "rgba(255,255,255,0.08)", borderRadius: 8, overflow: "hidden" }}>
                      <div style={{ height: "100%", width: `${b.value * bi}%`, background: i % 2 ? AMBER : CYAN, borderRadius: 8 }} />
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* کارت حلقه */}
          <div style={{ flex: 1, background: CARD, border: "1px solid rgba(255,255,255,0.1)", borderRadius: 24, padding: "36px 30px", display: "flex", flexDirection: "column", alignItems: "center", gap: 8 }}>
            <div style={{ position: "relative", display: "flex", alignItems: "center", justifyContent: "center" }}>
              <Ring p={ringP} />
              <div style={{ position: "absolute", fontSize: 58, fontWeight: 900, color: "#fff", direction: "ltr" }}>{count}%</div>
            </div>
            <div style={{ fontSize: 26, color: "#C8D3E4", marginTop: 8 }}>پیشرفت پروژه</div>
          </div>
        </div>

        <div style={{ display: "flex", gap: 18, fontSize: 24, color: "#7E8CA6", direction: "rtl" }}>
          <span>داده · نمودار · اعتماد</span>
          <span style={{ direction: "ltr" }}>· 30fps · 1920×1080</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
