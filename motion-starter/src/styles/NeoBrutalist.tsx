import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { FONT } from "../lib/font";

/**
 * سبک گرافیکی ۰۵ — نئو-بروتالیست (Neo-brutalism)
 * رنگ‌های اشباع، حاشیه‌ی ضخیم مشکی، سایه‌ی آفست سخت، تایپ درشت، برچسب‌های کج.
 * زبان بصری: جسور، خیابانی، استارتاپ جوان، محتوای وایرال.
 */

const YELLOW = "#E9FF3D";
const BLACK = "#0A0A0A";
const PINK = "#FF5CA8";
const BLUE = "#4E7CFF";

const Marquee: React.FC<{ top: number; dir: number; color: string; bg: string; text: string }> = ({ top, dir, color, bg, text }) => {
  const frame = useCurrentFrame();
  const x = ((frame * 6 * dir) % 900 + 900) % 900;
  return (
    <div style={{ position: "absolute", top, left: 0, right: 0, background: bg, borderTop: `5px solid ${BLACK}`, borderBottom: `5px solid ${BLACK}`, overflow: "hidden", padding: "10px 0" }}>
      <div style={{ display: "flex", whiteSpace: "nowrap", transform: `translateX(${dir > 0 ? x - 900 : -x}px)`, fontFamily: FONT, fontWeight: 900, fontSize: 42, color }}>
        {Array.from({ length: 8 }).map((_, i) => (
          <span key={i} style={{ padding: "0 34px" }}>{text} ✶</span>
        ))}
      </div>
    </div>
  );
};

export const NeoBrutalist: React.FC = () => {
  const frame = useCurrentFrame();
  const pop = interpolate(frame, [0, 10], [0, 1], { extrapolateRight: "clamp" });
  const tilt = interpolate(frame, [0, 150], [3, -2]);

  return (
    <AbsoluteFill style={{ background: YELLOW, direction: "rtl", fontFamily: FONT, overflow: "hidden" }}>
      {/* مربع‌های شکسته */}
      <div style={{ position: "absolute", right: -80, top: 120, width: 320, height: 320, background: BLUE, border: `6px solid ${BLACK}`, transform: `rotate(${tilt * 2}deg)` }} />
      <div style={{ position: "absolute", left: 60, bottom: 200, width: 180, height: 180, background: PINK, border: `6px solid ${BLACK}`, borderRadius: "50%", transform: `rotate(${-tilt}deg)` }} />

      <Marquee top={0} dir={1} color={BLACK} bg={PINK} text="موشن" />
      <Marquee top={1010} dir={-1} color={YELLOW} bg={BLACK} text="VIDEO" />

      <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
        <div
          style={{
            transform: `scale(${interpolate(pop, [0, 1], [0.6, 1])}) rotate(${tilt}deg)`,
            opacity: pop,
            background: "#fff",
            border: `7px solid ${BLACK}`,
            boxShadow: `16px 16px 0 ${BLACK}`,
            padding: "64px 76px",
            maxWidth: 1150,
          }}
        >
          <div style={{ fontSize: 34, fontWeight: 900, background: BLACK, color: YELLOW, display: "inline-block", padding: "8px 22px", marginBottom: 26, letterSpacing: 4, direction: "ltr" }}>
            NEW DROP
          </div>
          <div style={{ fontSize: 136, fontWeight: 900, color: BLACK, lineHeight: 1.12, letterSpacing: -3 }}>
            ایده، حرکت،
            <br />
            ویدیو
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
