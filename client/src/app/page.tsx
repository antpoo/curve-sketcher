"use client";
import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

function Home() {

  // state variable for user inputted equation
  const [userEquation, setUserEquation] = useState("");

  // router object 
  const router = useRouter();

  // submitting user equation and bringing user to start page
  const handleUserSubmit = (e : React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    router.push(`/start?expression=${encodeURIComponent(userEquation)}`);
  };


  return (
    <div className="flex flex-col items-center justify-center h-screen">
      {/* form for user to input equation */}
      <form onSubmit={handleUserSubmit} className="flex flex-col gap-y-4">
        <label>
          Enter your equation: 
          <input 
            type="text" 
            value={userEquation} 
            onChange={e => setUserEquation(e.target.value)}
            className="border rounded mx-2" />
        </label>
        {/* submit button */}
        <input 
          type="submit" 
          value="Submit" 
          className="bg-blue-300 cursor-pointer" />
      </form>

    </div>
  );
}

export default Home;