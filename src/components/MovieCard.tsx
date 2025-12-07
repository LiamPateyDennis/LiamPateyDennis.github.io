import "../css/MovieCard.css";

interface Movie {
  title: string;
  url?: string;
  poster_path: string;
  release_date: string;
  id: number;
}

interface MovieCardProps {
  movie: Movie;
}

function MovieCard({ movie }: MovieCardProps) {
  function onFavoriteClick() {
    alert("clicked");
  }
  return (
    <>
      <div className="movie-card">
        <div className="movie-poster">
          <img
            src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`}
            alt={movie.title}
          ></img>
        </div>
        <div className="movie-overlay">
          <button className="favourite-btn" onClick={onFavoriteClick}>
            ❤︎
          </button>
        </div>
      </div>
      <div className="movie-info">
        <h3>{movie.title}</h3>
        <p>{movie.release_date?.split("-")[0]}</p>
      </div>
    </>
  );
}

export default MovieCard;
