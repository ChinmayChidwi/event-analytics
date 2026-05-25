"use client";

import { useEffect, useState } from "react";
import api from "../lib/api";


export default function DashboardPage() {

  const [totalEvents, setTotalEvents] =
    useState(0);

const [eventsByType, setEventsByType] =
  useState<any[]>([]);


  useEffect(() => {

    fetchAnalytics();

  }, []);

  useEffect(() => {

  const socket = new WebSocket(
    "ws://127.0.0.1:8000/ws/events"
  );
socket.onmessage = async (event) => {

  console.log(
    "LIVE EVENT RECEIVED:",
    event.data
  );

  setTimeout(async () => {

    await fetchAnalytics();

  }, 1000);
};

  return () => {

    socket.close();
  };

}, []);

const fetchAnalytics = async () => {

  try {

    const token =
      localStorage.getItem("token");

    const summaryResponse =
      await api.get(
        "/analytics/summary",
        {
          headers: {
            Authorization:
              `Bearer ${token}`
          }
        }
      );

    const typeResponse =
      await api.get(
        "/analytics/events-by-type",
        {
          headers: {
            Authorization:
              `Bearer ${token}`
          }
        }
      );

    console.log(
      "UPDATED ANALYTICS:",
      typeResponse.data
    );

    setTotalEvents(
      Number(
        summaryResponse.data.total_events
      )
    );

    setEventsByType(
      JSON.parse(
        JSON.stringify(
          typeResponse.data
        )
      )
    );

  } catch (error) {

    console.error(error);
  }
};
  return (

    <div className="p-10 bg-gray-100 min-h-screen">

      <h1 className="text-4xl font-bold mb-8">
        Analytics Dashboard
      </h1>


      <div className="bg-white p-6 rounded-lg shadow mb-8 w-[300px]">

        <h2 className="text-xl mb-2">
          Total Events
        </h2>

        <p className="text-5xl font-bold">
          {totalEvents}
        </p>

      </div>


      <div className="bg-white p-6 rounded-lg shadow">

        <h2 className="text-2xl font-bold mb-4">
          Events By Type
        </h2>

        <div className="space-y-4">

          {eventsByType.map((event: any) => (

            <div
              key={event.event_type}
              className="flex justify-between border-b pb-2"
            >

              <span>
                {event.event_type}
              </span>

              <span className="font-bold">
                {event.count}
              </span>

            </div>

          ))}

        </div>

      </div>

    </div>
  );
}