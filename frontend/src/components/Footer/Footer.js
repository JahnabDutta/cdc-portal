import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Tooltip from '@material-ui/core/Tooltip';
import IconButton from '@material-ui/core/IconButton';
import FacebookIcon from '@material-ui/icons/Facebook';
import LinkedInIcon from '@material-ui/icons/LinkedIn';
import GitHubIcon from '@material-ui/icons/GitHub';
function Copyright() {
  return (
    <Typography variant="body2" style={{ color: '#012970' }} align="center">
      {'Copyright © '}
      <Link color="inherit">CDC, IITJ</Link> {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const footers = [
  {
    title: 'Downloads',
    description: [
      ['JAF', '/jaf'],
      ['IAF', '/iaf'],
      ['Brochure', '/brochure'],
    ],
  },
  {
    title: 'Quick Links',
    description: [
      ['Placement registration link', '/recruiter-login'],
      ['Placement Statistics', '/placement-statistics'],
      ['Meet our Team', '/c3-members'],
      ['AIPC Norms', '/aipc-norms'],
    ],
  },
  {
    title: 'External Links',
    description: [
      ['IIT Jodhpur', 'https://iitj.ac.in/'],
      ['Student Gymkhana', 'https://students.iitj.ac.in/'],
    ],
  },
];

const useStyles = makeStyles((theme) => ({
  footer: {
    backgroundColor: 'white',
    backgroundSize: 'cover',
    background: 'url(https://i.imgur.com/VcAY65E.jpeg) top center no-repeat',
    color: '#012970',
    padding: theme.spacing(3, 0),
  },
  '@global': {
    ul: {
      margin: 0,
      padding: 0,
      listStyle: 'none',
    },
  },
}));

export default function Footer(props) {
  const classes = useStyles();

  return (
    <>
      <footer className={classes.footer}>
        <Grid container style={{ paddingLeft: '7%' }}>
          <Grid item xs={6} sm={3}>
            <Typography
              component={'span'}
              variant="h6"
              align="center"
              gutterBottom
            >
              <ul align="left">
                <li>
                  <Typography style={{ color: '#012970' }} variant="h6">
                    <b>CDC IITJ</b>
                  </Typography>
                </li>
                <li>
                  <Typography variant="subtitle1" style={{ color: '#012970' }}>
                    Indian Institute of Technology Jodhpur
                  </Typography>
                  <Typography variant="subtitle1" style={{ color: '#012970' }}>
                    NH 65 Nagaur Road
                  </Typography>
                  <Typography variant="subtitle1" style={{ color: '#012970' }}>
                    Karwar 342037, Jodhpur District
                  </Typography>
                </li>
                <li>
                  <Typography variant="subtitle1" style={{ color: '#012970' }}>
                    <b>Phone:</b> +91 291 2801154
                  </Typography>
                  <Typography variant="subtitle1" style={{ color: '#012970' }}>
                    <b>Phone:</b> +91 291 2801153
                  </Typography>
                  <Typography variant="subtitle1" style={{ color: '#012970' }}>
                    <b>Email:</b>{' '}
                    <a
                      href="mailto:placement@iitj.ac.in"
                      style={{ textDecoration: 'none', color: '#012970' }}
                    >
                      placement@iitj.ac.in
                    </a>
                  </Typography>
                </li>
              </ul>
            </Typography>
          </Grid>
          {footers.map((footer) => (
            <Grid item xs={6} sm={3} key={footer.title}>
              <Typography
                component={'span'}
                style={{ color: '#012970' }}
                variant="h6"
                gutterBottom
              >
                <b>{footer.title}</b>
              </Typography>
              <ul>
                {footer.description.map((item) => (
                  <li key={item}>
                    <Link
                      href={item[1]}
                      target="_blank"
                      rel="noopener noreferrer"
                      variant="subtitle1"
                      style={{ color: '#012970' }}
                    >
                      {item[0]}
                    </Link>
                  </li>
                ))}
              </ul>
            </Grid>
          ))}
        </Grid>
      </footer>
      <Container style={{ background: '#f6f9ff', padding: '20px 0' }}>
        <Typography component={'span'} variant="h6" align="center" gutterBottom>
          <div>
            <Tooltip arrow title="facebook">
              <IconButton
                href="https://www.facebook.com/SPC.IITJ/"
                target="_blank"
                rel="noopener noreferrer"
                variant="outlined"
                style={{ color: '#012970' }}
              >
                <FacebookIcon />
              </IconButton>
            </Tooltip>
            <Tooltip arrow title="Linkedin">
              <IconButton
                href="https://in.linkedin.com/in/career-development-cell-iit-jodhpur-62a31352"
                target="_blank"
                rel="noopener noreferrer"
                style={{ color: '#012970' }}
                variant="outlined"
              >
                <LinkedInIcon style={{ color: '#012970' }} />
              </IconButton>
            </Tooltip>
            <Tooltip arrow title="GitHub">
              <IconButton
                href="https://github.com/devlup-labs/cdc-portal"
                target="_blank"
                rel="noopener noreferrer"
                variant="outlined"
                style={{ color: '#012970' }}
              >
                <GitHubIcon />
              </IconButton>
            </Tooltip>
          </div>
        </Typography>
        <Typography
          variant="subtitle1"
          align="center"
          style={{ color: '#012970' }}
          component="p"
        >
          Designed & Maintained by Career Development Cell, IIT Jodhpur
        </Typography>
        <Copyright />
      </Container>
    </>
  );
}
