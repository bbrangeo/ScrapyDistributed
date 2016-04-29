$.fn.charts = function (categories, data, title) {

    var colors = Highcharts.getOptions().colors,
        name = 'Count of Crawled Items';

    function setChart(name, categories, data, color) {
        chart.xAxis[0].setCategories(categories, false);
        chart.series[0].remove(false);
        chart.addSeries({
            name: name,
            data: data,
            color: color || 'white'
        }, false);
        chart.redraw();
    }

    var chart = $(this).highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: title
        },
        xAxis: {
            categories: categories
        },
        yAxis: {
            title: {
                text: 'Total Items'
            }
        },
        plotOptions: {
            column: {
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    color: colors[0],
                    style: {
                        fontWeight: 'bold'
                    },
                    formatter: function () {
                        return 'count' + this.y;
                    }
                }
            }
        },
        tooltip: {
            formatter: function () {
                return 'Crawled ' + this.y + ' items';
            }
        },
        series: [{
            name: name,
            data: data,
            color: 'white'
        }],
        exporting: {
            enabled: false
        },
        credits: {
            text: ''
        }
    }).highcharts();


};
