import React, { useState, useEffect } from 'react';
import instance from '../api/axios';
import Loading from '../components/Loading';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import { Container, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import FadeInWhenVisible from '../components/Animation/FadeIn';
import FadeUpWhenVisible from '../components/Animation/FadeUp';

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
}));

const StudentGuidelines = () => {
  const classes = useStyles();
  const [loading, setLoding] = useState(true);
  const [StudentGuidelines, setStudentGuidelines] = useState([]);

  useEffect(() => {
    instance
      .get('main/navbar_suboptions/')
      .then((res) => {
        setStudentGuidelines(
          res.data.filter((subOption) =>
            subOption.title.includes('StudentGuidelines')
          )[0]
        );
      })
      .then(() => setLoding(false))
      .catch((error) => console.log(error));
  }, []);

  const createStudentGuidelines = () => {
    return { __html: StudentGuidelines.description };
  };

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
                  <Paper className={classes.paper}>
                    <Typography
                      component="h5"
                      variant="h5"
                      style={{ fontSize: 30, textAlign: 'center' }}
                    >
                      Norms/Guidelines
                    </Typography>
                  </Paper>
                </FadeInWhenVisible>
              </Grid>
              <Grid item xs={12}>
                <FadeUpWhenVisible>
                  <Paper className={classes.paper}>
                    {StudentGuidelines ? (
                      <p dangerouslySetInnerHTML={createStudentGuidelines()} />
                    ) : (
                      <p>Coming soon...</p>
                    )}
                  </Paper>
                </FadeUpWhenVisible>
              </Grid>
            </Grid>
          </Container>
        </>
      )}
    </div>
  );
};

export default StudentGuidelines;
