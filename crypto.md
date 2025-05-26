---
layout: default
title: Crypto Trading Performance
permalink: /crypto/
---

<h1>📈 Trading Performance</h1>
<div id="trading-performance"></div>

<h2>Equity History</h2>
<canvas id="equity-chart" width="100%" height="100"></canvas>

<script>
    fetch('/images/crypto-trading-history.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('trading-performance');

            const currentData = data.history[data.history.length - 1];
            const equity = parseFloat(currentData.total_equity);
            const previousEquity = data.history.length > 1
                ? parseFloat(data.history[data.history.length - 2].total_equity)
                : equity;

            const diff = equity - previousEquity;
            const diffPercent = ((diff / previousEquity) * 100).toFixed(2);
            const isUp = diff >= 0;

            const arrow = isUp ? '▲' : '▼';
            const color = isUp ? 'green' : 'red';

            const positionRows = currentData.all_future_position.map(pos => `
                <tr>
                    <td>${pos.symbol}</td>
                    <td><span <span style="background-color: ${parseFloat(pos.ROI) >= 0 ? 'green' : 'red'}; color: white; padding: 3px 8px; border-radius: 12px; font-size: 0.85em;">${pos.leverage}x</span></td>
                    <td style="color: ${parseFloat(pos.ROI) >= 0 ? 'green' : 'red'}">
                    ${(parseFloat(pos.ROI) * 100).toFixed(2)}%
                    </td>
                </tr>
                `).join('');

            container.innerHTML = `
                <div style="text-align: center; margin-bottom: 30px;">
                    <h1 style="font-size: 3em;">$${currentData.total_equity}</h1>
                    <div style="font-size: 1.5em; color: ${color};">
                    ${arrow} ${diffPercent}%
                    </div>
                </div>

                <h2>Open Futures Positions</h2>
                <table style="width: 100%; border-collapse: collapse;">
                    <thead>
                    <tr>
                        <th style="text-align: left; padding: 8px;">Symbol</th>
                        <th style="text-align: left; padding: 8px;">Leverage</th>
                        <th style="text-align: left; padding: 8px;">ROI</th>
                    </tr>
                    </thead>
                    <tbody>
                    ${positionRows}
                    </tbody>
                </table>
            `;

            // Draw chart
            const ctx = document.getElementById('equity-chart').getContext('2d');

            const labels = (data.history || []).map(entry =>
            new Date(entry.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
            );

            const equityData = data.history.map(entry => parseFloat(entry.total_equity));

            new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                label: 'Total Equity ($)',
                data: equityData,
                borderColor: 'blue',
                backgroundColor: 'rgba(0, 123, 255, 0.1)',
                fill: true,
                tension: 0.3,
                pointRadius: 3,
                pointHoverRadius: 5
                }]
            },
            options: {
            responsive: true,
            scales: {
                x: {
                title: {
                    display: true,
                    text: 'Date',
                    font: {
                    size: 16
                    }
                },
                ticks: {
                    font: {
                    size: 14
                    }
                }
                },
                y: {
                title: {
                    display: true,
                    text: 'Equity ($)',
                    font: {
                    size: 16
                    }
                },
                ticks: {
                    font: {
                    size: 14
                    }
                }
                }
            },
            plugins: {
                legend: {
                display: false
                },
                tooltip: {
                bodyFont: {
                    size: 14
                },
                titleFont: {
                    size: 16
                }
                }
            }
            }
            });
    })
    .catch(error => {
        console.error('Error loading trading data:', error);
        document.getElementById('trading-performance').innerText = 'Failed to load trading performance.';
    });
</script>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
