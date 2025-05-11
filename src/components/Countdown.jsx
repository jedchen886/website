// src/components/Countdown.jsx
import React, { useState, useEffect } from 'react';

const Countdown = () => {
  // Set the target date to May 6, 2025 at midnight
  const targetDate = new Date('2025-05-06T00:00:00');

  // Calculate the number of days left until the target date
  const calculateDaysLeft = () => {
    const now = new Date();
    const diff = targetDate - now;
    // If the target date has passed, return 0
    return diff > 0 ? Math.ceil(diff / (1000 * 60 * 60 * 24)) : 0;
  };

  // Use state to store the days left
  const [daysLeft, setDaysLeft] = useState(calculateDaysLeft());

  // Set up an effect to update the countdown every day
  useEffect(() => {
    // Update every 24 hours (86,400,000 milliseconds)
    const intervalId = setInterval(() => {
      setDaysLeft(calculateDaysLeft());
    }, 86400000);

    // Cleanup the interval on component unmount
    return () => clearInterval(intervalId);
  }, []);

  return (
    <span className="ml-2 font-bold text-yellow-500">
      Only {daysLeft} day{daysLeft !== 1 ? 's' : ''} away!
    </span>
  );
};

export default Countdown;
