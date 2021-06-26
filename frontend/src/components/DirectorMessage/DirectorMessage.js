import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Container from '@material-ui/core/Container';
import { getLink } from '../../utils/getLink';
const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    width: '100%',
    height: 'auto',
    background: 'rgb(240,240,240)',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: -30,
    boxShadow: 'none',
  },
  MessageContainer: {
    width: '100%',
    height: 'auto',
    marginTop: 40,
    marginBottom: 40,
    zIndex: 2,
    display: 'flex',
    flexDirection: 'row',
    boxShadow: 'none',
    borderRadius: 20,
    [theme.breakpoints.down(780)]: {
      flexDirection: 'column',
      alignItems: 'center',
    },
  },
  MessageHeader: {
    fontSize: 40,
    marginBottom: '0.5%',
    marginTop: '0.5%',
  },
  details: {
    display: 'flex',
    flexDirection: 'column',
    width: '100%',
    marginBottom: 0,
  },
  content: {
    flex: '1 0 auto',
  },
  cover: {
    minWidth: 250,
    height: 250,
    margin: 30,
    boxShadow: '0 0 12px',
    borderRadius: '50%',
  },
}));

const DirectorMessageComponent = ({ data }) => {
  const classes = useStyles();
  const createDirectorMessage = () => {
    return { __html: data.content };
  };

  return (
    <Container maxWidth="lg">
      {data ? (
        <Card className={classes.MessageContainer}>
          <CardMedia
            component="div"
            className={classes.cover}
            image={getLink(data.image)}
          />
          <div className={classes.details}>
            <CardContent className={classes.content}>
              <h2 className={classes.MessageHeader}>{data.title}</h2>
              <div style={{ fontSize: '1rem', color: 'black' }}>
                <p dangerouslySetInnerHTML={createDirectorMessage()} />
                <p>{data.name}</p>
              </div>
            </CardContent>
          </div>
        </Card>
      ) : (
        ''
      )}
    </Container>
  );
};
export default DirectorMessageComponent;
