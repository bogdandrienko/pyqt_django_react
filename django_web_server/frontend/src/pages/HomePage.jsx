import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import axios from "axios";
import Navbar from "../components/navbar";
import Footer from "../components/footer";

export const IMAGE_LOAD = "IMAGE_LOAD_CONSTANT";
export const IMAGE_DATA = "IMAGE_DATA_CONSTANT";
export const IMAGE_ERROR = "IMAGE_ERROR_CONSTANT";
export const IMAGE_FAIL = "IMAGE_FAIL_CONSTANT";
export const IMAGE_RESET = "IMAGE_RESET_CONSTANT";

export const ImageAction = () => async (dispatch, getState) => {
  try {
    dispatch({
      type: IMAGE_LOAD,
    });

    const config = {
      method: "GET",
      timeout: 10000,
      url: `/api/get_images/`,
      data: null,
    };
    const response = await axios(config);
    console.log(response);

    const { data } = response;
    if (data) {
      dispatch({
        type: IMAGE_DATA,
        payload: data,
      });
    } else {
      dispatch({
        type: IMAGE_ERROR,
        payload: data,
      });
    }
  } catch (error) {
    console.log(error);
    dispatch({
      type: IMAGE_FAIL,
      payload: error,
    });
  }
};

export const ImageReducer = (state = {}, action = null) => {
  switch (action.type) {
    case IMAGE_LOAD:
      return { load: true };
    case IMAGE_DATA:
      return { load: false, data: action.payload };
    case IMAGE_ERROR:
      return { error: "ошибка на сервере" };
    case IMAGE_FAIL:
      return { fail: "ошибка на клиенте" };
    case IMAGE_RESET:
      return {};
    default:
      return state;
  }
};

export function HomePage() {
  const dispatch = useDispatch();

  const ImageStore = useSelector((state) => state.ImageStore);
  const { load: load, data: data, error: error, fail: fail } = ImageStore;

  const getImages = () => {
    dispatch(ImageAction());
  };

  const resetImages = () => {
    dispatch({ type: IMAGE_RESET });
  };

  useEffect(() => {
    console.log(`load: ${load}`);
    console.log(`data: ${data}`);
    console.log(`error: ${error}`);
    console.log(`fail: ${fail}`);
  }, [ImageStore]);

  return (
    <div>
      <main className="custom_main p-0 m-0 w-100">
        <Navbar />
        <div style={{ margin: "50px" }}>
          <div className="d-flex row align-content-between">
            <h1 className="col-6 text-success">BACKEND</h1>
            <h1 className="col-6 text-primary">FRONTEND</h1>
          </div>
          <div className="d-flex row align-content-between">
            <h5 className="col-6">
              Django{" "}
              <small className="small text-secondary">
                (VM / *nix / nginx / gunicorn / django-rest-framework /
                django-grappelli / django-cors-headers)
              </small>
            </h5>
            <h5 className="col-6">
              React{" "}
              <small className="small text-secondary">
                (typescript / redux / router-dom / axios)
              </small>
            </h5>
          </div>

          <hr />

          <div className="btn-group">
            <button
              className="btn btn-lg btn-outline-primary"
              onClick={getImages}
            >
              check
            </button>
            <button
              className="btn btn-lg btn-outline-secondary"
              onClick={resetImages}
            >
              reset
            </button>
          </div>

          <div className="">
            {load && (
              <div className="card m-1 p-1 text-primary">Идёт загрузка...</div>
            )}
            {data &&
              data.result &&
              (data.result.length <= 0 ? (
                <div className="card m-1 p-1 text-danger">Данных нет!</div>
              ) : (
                <ul className="card m-1 p-1 list-group mb-3">
                  {data.result.map((x) => (
                    <li
                      key={x.id}
                      className="list-group-item d-flex justify-content-between lh-sm"
                    >
                      <div>
                        <h6 className="my-0">{x.title}</h6>
                        <img
                          src={`/static/${x.image}`}
                          alt="изображение отсутствует"
                        />
                      </div>
                      <span className="text-muted">#{x.id}</span>
                    </li>
                  ))}
                </ul>
              ))}
            {error && <div className="card m-1 p-1 text-danger">{error}</div>}
            {fail && <div className="card m-1 p-1 text-warning">{fail}</div>}
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default HomePage;
