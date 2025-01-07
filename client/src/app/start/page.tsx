"use client";
import { useSearchParams } from "next/navigation";
import React, { useEffect, useState } from "react";

function Start() {

    // getting expression form URL 
    const searchParams = useSearchParams();
    const expression = searchParams.get("expression");

    // state variables 
    const [firstDerivative, setFirstDerivative] = useState("");
    const [secondDerivative, setSecondDerivative] = useState("");
    const [yIntercept, setYIntercept] = useState("");
    const [roots, setRoots] = useState([]);
    const [extrema, setExtrema] = useState([]);
    const [inflectionPoints, setInflectionPoints] = useState([]);
    const [verticalAsymptotes, setVerticalAsymptotes] = useState([]);
    const [horizontalAsymptotes, setHorizontalAsymptotes] = useState([]);


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
            setExtrema(data.extrema);
            setInflectionPoints(data.inflectionPoints);
            setVerticalAsymptotes(data.verticalAsymptotes);
            setHorizontalAsymptotes(data.horizontalAsymptotes);
        })
        .catch(error => console.log(error));
    }, []);

    return (
        <div>{expression}</div>
    );
}

export default Start;