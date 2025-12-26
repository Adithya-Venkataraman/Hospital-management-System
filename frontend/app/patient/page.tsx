"use client";
import React, { useEffect, useState } from "react";
export default function PatientPage() {
const [patients, setPatients] = useState<any[]>([]);
useEffect(() => {
  fetch("http://127.0.0.1:5000/doctor/1")
    .then((res) => res.json())
    .then((data) => {
      console.log("Fetched patients:", data);
      setPatients(data);
    })
    .catch((error) => {
      console.error("Error fetching patients:", error);
    });
}, []);

      
  return (
    <div style={{ padding: "20px" }}>
      <h2>Patient Dashboard</h2>
      <p>Welcome, Patient</p>
      {patients.map((p) => (
        <p key={p.patient_id}>{p.patient_name}</p>
    ))}

    </div>
    
  );
  
}
