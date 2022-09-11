import React, { useState, useEffect } from 'react';
import instance from '../../api/axios';
import Loading from '../Loading';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import { Container } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import FadeInWhenVisible from '../Animation/FadeIn';
import Iframe from 'react-iframe';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    display: 'flex',
    marginBottom: '2rem',
    [theme.breakpoints.down(460)]: {
      padding: 15,
    },
  },
  paper: {
    padding: theme.spacing(2),
    [theme.breakpoints.up(460)]: {
      paddingInline: 40,
    },
    width: 'auto',
    fontSize: '1rem',
    color: 'black',
  },
  text: {
    color: 'rgb(0,0,0)',
    fontsize: '1rem',
    marginTop: '4%',
    marginBottom: '2%',
  },
  heading: {
    fontSize: '1.8rem',
    color: '#fff',
    backgroundColor: '#012970',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '1rem',
  },
  iframe: {
    width: '100%',
    height: '50vh',
  },
}));

const PlacementCalendar = () => {
  const classes = useStyles();
  const [loading, setLoding] = useState(false);
  const [calendarLink, setcalendarLink] = useState('');

  useEffect(() => {
    instance
      .get('main/sheets_placement_calendar/')
      .then((res) => {
        const batch = localStorage
          .getItem('cdc_Dname')
          .split('(')[1]
          .substring(0, 3);
        console.log(batch);
        res.data.forEach((calender) => {
          const applicable_years = calender.applicable_years.split(',');
          console.log(applicable_years);
          if (applicable_years.includes(batch)) {
            setcalendarLink(calender.calendar_publish_link);
            console.log(calender.calendar_publish_link);
          }
        });
      })
      .then(() => setLoding(false))
      .catch((error) => console.log(error));
  }, []);

  return (
    <div style={{ height: 'auto', width: '100%' }}>
      {loading ? (
        <Loading />
      ) : (
        <>
          <Container maxWidth="lg" className={classes.root}>
            <Grid container spacing={3}>
              <Grid style={{ marginTop: '30px' }} item xs={12}>
                <FadeInWhenVisible>
                  <Paper
                    className={classes.heading}
                    style={{ background: '#012970', color: '#fff' }}
                    elevation={2}
                  >
                    <i
                      class="fas fa-calendar-alt"
                      style={{ margin: '0 1.2rem', padding: '0' }}
                    ></i>
                    Placement Calendar
                  </Paper>
                </FadeInWhenVisible>
              </Grid>
              <Grid item xs={12}>
                <div className={classes.iframe}>
                  {loading ? (
                    <h2>Loading...</h2>
                  ) : (
                    <Iframe
                      src={loading ? '#' : calendarLink}
                      width="100%"
                      height="140%"
                    />
                  )}
                </div>
              </Grid>
            </Grid>
          </Container>
        </>
      )}
    </div>
  );
};

export default PlacementCalendar;
