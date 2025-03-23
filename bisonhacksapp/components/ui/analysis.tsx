"use client";
import { useEffect, useState } from "react";


const AnalysisResult = ({ gene }: { gene: string }) => {
  const [analysis, setAnalysis] = useState("");
  const [hasUpdated, setHasUpdated] = useState(false);

  useEffect(() => {
    setHasUpdated(false);
    const fetchEvoResults = async () => {
      const res = await fetch(`/api/analysis?gene=${gene}`);
      const data = await res.json();
      setAnalysis(data.analysis);
    };

    fetchEvoResults();
    setHasUpdated(true);
  }, [gene]);
  return (
    <div className="flex flex-col gap-4">
      {hasUpdated ? <p>Analysis: Possible {analysis}</p> : <p>Loading...</p>}
    </div>
  );
};

export default AnalysisResult;
