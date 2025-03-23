"use client";
import { GaugeComponent } from "react-gauge-component";

const Guage = ({
  name,
  limits,
  max,
  min,
  value,
  unit,
  range_type,
}: {
  name: string;
  limits: number[];
  max: number;
  min: number;
  value: number;
  unit: string;
  range_type?: string;
}) => {
  var colors = ["#EA4228", "#F5CD19", "#5BE12C", "#F5CD19", "#EA4228"];
  var texts = ["Too low", "Low", "OK", "High", "Too high"];
  if (range_type === "inc") {
    colors = ["#5BE12C", "#F5CD19", "#F5CD19", "#EA4228", "#EA4228"];
    texts = ["OK", "High", "High", "Too high", "Too high"];
  }
  if (range_type === "dec") {
    colors = ["#EA4228", "#EA4228", "#F5CD19", "#F5CD19", "#5BE12C"];
    texts = ["Too low", "Too low", "Low", "Low", "OK"];
  }
  return (
    <div className="flex flex-col items-center justify-center">
      <GaugeComponent
        className="w-100 h-45"
        type="semicircle"
        arc={{
          width: 0.2,
          padding: 0.000,
          cornerRadius: 2,
          // gradient: true,
          subArcs: [
            {
              limit: limits[0],
              color: colors[0],
              showTick: true,
              tooltip: {
                text: `${texts[0]} ${name}!`,
              },
              onClick: () => console.log(""),
              onMouseMove: () => console.log(""),
              onMouseLeave: () => console.log(""),
            },
            {
              limit: limits[1],
              color: colors[1],
              showTick: true,
              tooltip: {
                text: `${texts[1]} ${name}!`,
              },
            },
            {
              limit: limits[2],
              color: colors[2],
              showTick: true,
              tooltip: {
                text: `${texts[2]} ${name}!`,
              },
            },
            {
              limit: limits[3],
              color: colors[3],
              showTick: true,
              tooltip: {
                text: `${texts[3]} ${name}!`,
              },
            },
            {
              color: colors[4],
              tooltip: {
                text: `${texts[4]} ${name}!`,
              },
            },
          ],
        }}
        pointer={{
          color: "#000",
          length: 0.7,
          width: 10,
          elastic: true,
        }}
        labels={{
          valueLabel: { formatTextValue: (value) => value + unit },
          tickLabels: {
            type: "outer",
            defaultTickValueConfig: {
              formatTextValue: (value: any) => value + unit,
              style: { fontSize: 10 },
            },
            ticks: [{ value: 13 }, { value: 22.5 }, { value: 32 }],
          },
        }}
        value={value}
        minValue={min}
        maxValue={max}
      />
      <p>{name}</p>
    </div>
  );
};

export default Guage;
