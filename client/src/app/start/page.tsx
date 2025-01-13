"use client";
import { useSearchParams } from "next/navigation";
import React, { useEffect, useState } from "react";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";
import { Scatter } from "react-chartjs-2";

ChartJS.register(CategoryScale, LinearScale, PointElement, Title, Tooltip, Legend);

function Start() {

    // getting expression form URL 
    const searchParams = useSearchParams();
    const expression = searchParams.get("expression");

    // state variables 
    const [firstDerivative, setFirstDerivative] = useState("");
    const [secondDerivative, setSecondDerivative] = useState("");
    const [yIntercept, setYIntercept] = useState("");
    const [roots, setRoots] = useState([]);
    const [localMaxs, setLocalMaxs] = useState([[]]);
    const [localMins, setLocalMins] = useState([[]]);
    const [inflectionPoints, setInflectionPoints] = useState([[]]);
    const [verticalAsymptotes, setVerticalAsymptotes] = useState([]);
    const [horizontalAsymptotes, setHorizontalAsymptotes] = useState([]);
    const [graphData, setGraphData] = useState([]);

    const radius: number = 5;


    // getting all info from Flask server
    useEffect(() => {
        fetch(`http://localhost:8080/api/equation`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ expression })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            setFirstDerivative(data.firstDerivative);
            setSecondDerivative(data.secondDerivative);
            setYIntercept(data.yIntercept);
            setRoots(data.roots);
            setLocalMaxs(data.extrema[0]);
            setLocalMins(data.extrema[1]);
            setInflectionPoints(data.inflectionPoints);
            setVerticalAsymptotes(data.verticalAsymptotes);
            setHorizontalAsymptotes(data.horizontalAsymptotes);
        })
        .catch(error => console.log(error));
    }, []);

    return (
        <div className="flex flex-col items-center justify-center h-screen">
            {/* table of all important function data */}
            <table>
                <tbody>
                    <tr>
                        <th>First Derivative:</th>
                        <th>{firstDerivative}</th>
                    </tr>
                    <tr>
                        <th>Second Derivative:</th>
                        <th>{secondDerivative}</th>
                    </tr>
                    <tr>
                        <th>y-intercept:</th>
                        <th>{yIntercept}</th>
                    </tr>
                    <tr>
                        <th>Roots:</th>
                        <th>{roots.length == 0 ? "None" : roots.join(", ")}</th>
                    </tr>
                    <tr>
                        <th>Local Maxima:</th>
                        <th>{localMaxs[0].length == 0 ? "None" : localMaxs[0].join(", ")}</th>
                    </tr>
                    <tr>
                        <th>Local Minima:</th>
                        <th>{localMins[0].length == 0 ? "None" : localMins[0].join(", ")}</th>
                    </tr>
                    <tr>
                        <th>Points of Inflection:</th>
                        <th>{inflectionPoints[0].length == 0 ? "None" : inflectionPoints[0].join(", ")}</th>
                    </tr>
                    <tr>
                        <th>Vertical Asymptotes:</th>
                        <th>{verticalAsymptotes.length == 0 ? "None" : verticalAsymptotes.join(", ")}</th>
                    </tr>
                    <tr>
                        <th>Horizontal Asymptotes/Limits:</th>
                        <th>{horizontalAsymptotes.length == 0 ? "None" : horizontalAsymptotes.join(", ")}</th>
                    </tr>
                </tbody>
            </table>

            
        </div>
    );
}

export default Start;